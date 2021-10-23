"""
Provides linkedin api-related code
"""
import random
import logging
from time import sleep
from urllib.parse import urlencode
import json
import re
from fajita import Fajita

import seek_com_au.settings as settings
from seek_com_au.objects.search_listing import get_search_listing
from seek_com_au.objects.listing import get_listing

logger = logging.getLogger(__name__)


class SeekComAu(Fajita):
    """
    Class for accessing seek.com.au API.
    """

    API_BASE_URL = "https://www.seek.com.au/api"
    REQUEST_HEADERS = {
        "content-type": "application/json",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
    }

    def __init__(
        self, proxies={}, debug=False,
    ):
        Fajita.__init__(
            self,
            base_url=self.API_BASE_URL,
            headers=self.REQUEST_HEADERS,
            proxies=proxies,
            debug=debug,
            cookie_directory=settings.COOKIE_PATH,
        )
        logging.basicConfig(level=logging.DEBUG if debug else logging.INFO)
        self.logger = logger

    def search(
        self,
        limit=-1,
        location="All Australia",
        keywords="",
        exclude_keywords=[]
    ):
        def get_query_params(page=1):
            query_variables = {
                "siteKey": "AU-Main",
                "sourcesystem": "houston",
                "where": location,
                "page": page,
                "seekSelectAllPages": "true",
                "hadPremiumListings": "true",
            }
            if keywords:
                query_variables["keywords"] = keywords
            return query_variables

        def parse_items(res):
            data = res.json()
            listings = [get_search_listing(listing)
                        for listing in data.get('data', [])]

            # filter listings that contain exclude_keywords
            if exclude_keywords:
                pattern = re.compile("|".join(exclude_keywords))
                listings = [
                    listing
                    for listing in listings
                    if not re.search(pattern, " ".join(listing.bullet_points) + " " + listing.teaser)
                ]

            return listings

        def get_current_page(**kwargs):
            return kwargs["params"]["page"]

        def next_page(**kwargs):
            current_page = get_current_page(**kwargs)
            kwargs["params"] = get_query_params(current_page + 1)

            return kwargs

        def is_done(items, res, **kwargs):
            if not items:
                return True

            items_count = len(items)
            if limit > -1:
                if items_count >= limit:
                    return True

            data = res.json()
            listings = data.get('data', [])
            if not listings:
                return True

            return False

        listings = self._scroll(
            "/chalice-search/search",
            "GET",
            parse_items,
            next_page,
            is_done,
            params=get_query_params()
        )

        return listings

    def get_listing(self, listing_id, ):
        res = self._get(
            f"/job/{listing_id}",
            base_url="https://chalice-experience-api.cloud.seek.com.au",
            params={"zone": "anz-1",
                    "locale": "AU",
                    "isSourcrEnabled": "true"}
        )
        listing = res.json()

        return get_listing(listing)
