from dataclasses import dataclass, field
import re
from seek_com_au.utils import delete_nulls


@dataclass
class Advertiser:
    id: str
    description: str


@dataclass
class SubClassification:
    id: str
    description: str


@dataclass
class Classification:
    id: str
    description: str


@dataclass
class SearchListing:
    id: str
    area: str
    teaser: str
    title: str
    work_type: str
    salary: str
    company_name: str
    listing_date: str
    role_id: str
    location: str
    location_id: int
    location_where_value: str
    suburb_id: int
    suburb_where_value: str
    bullet_points: list[str]
    classification: Classification
    sub_classification: SubClassification
    advertiser: Advertiser


def get_advertiser(search_listing):
    advertiser = search_listing.get('advertiser', {})
    return Advertiser(
        id=advertiser.get('id'),
        description=advertiser.get('description')
    )


def get_classification(search_listing):
    classification = search_listing.get('classification', {})
    return Classification(
        id=classification.get('id'),
        description=classification.get('description')
    )


def get_sub_classification(search_listing):
    sub_classification = search_listing.get('subClassification', {})
    return SubClassification(
        id=sub_classification.get('id'),
        description=sub_classification.get('description')
    )


def get_search_listing(search_listing):
    return SearchListing(
        id=search_listing.get("id"),
        area=search_listing.get('area'),
        teaser=search_listing.get('teaser'),
        title=search_listing.get('title'),
        work_type=search_listing.get('workType'),
        salary=search_listing.get('salary'),
        company_name=search_listing.get('companyName'),
        listing_date=search_listing.get('listingDate'),
        role_id=search_listing.get('roleId'),
        location=search_listing.get('location'),
        location_id=search_listing.get('locationId'),
        location_where_value=search_listing.get('locationWhereValue'),
        suburb_id=search_listing.get('suburbId'),
        suburb_where_value=search_listing.get('suburbWhereValue'),
        bullet_points=search_listing.get('bulletPoints'),
        classification=get_classification(search_listing),
        sub_classification=get_sub_classification(search_listing),
        advertiser=get_advertiser(search_listing),
    )
