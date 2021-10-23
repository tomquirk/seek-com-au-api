from dataclasses import dataclass


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
class Company:
    id: str
    name: str


@dataclass
class Location:
    area: str
    city: str
    nation: str
    state: str
    suburb: str


@dataclass
class Listing:
    id: str
    title: str
    work_type: str
    status: str
    salary: str
    salary_type: str
    listing_date: str
    location_id: int
    job_ad_details: str
    role_titles: str
    state_id: int
    classification: Classification
    sub_classification: SubClassification
    advertiser: Advertiser
    company: Company
    location: Location


def get_advertiser(listing):
    advertiser = listing.get('advertiser', {})
    return Advertiser(
        id=advertiser.get('id'),
        description=advertiser.get('description')
    )


def get_classification(listing):
    classification = listing.get('classification', {})
    return Classification(
        id=classification.get('id'),
        description=classification.get('description')
    )


def get_sub_classification(listing):
    sub_classification = listing.get('subClassification', {})
    return SubClassification(
        id=sub_classification.get('id'),
        description=sub_classification.get('description')
    )


def get_location(listing):
    location = listing.get('locationHierarchy', {})
    return Location(
        area=location.get('area'),
        city=location.get('city'),
        nation=location.get('nation'),
        state=location.get('state'),
        suburb=location.get('suburb'),
    )


def get_company(listing):
    company = listing.get('companyReview', {})
    return Company(
        id=company.get('companyId'),
        name=company.get('companyName'),
    )


def get_listing(listing):
    return Listing(
        id=listing.get("id"),
        status=listing.get('status'),
        title=listing.get('title'),
        work_type=listing.get('workType'),
        salary=listing.get('salary'),
        salary_type=listing.get('salaryType'),
        listing_date=listing.get('listingDate'),
        location_id=listing.get('locationId'),
        job_ad_details=listing.get('jobAdDetails'),
        role_titles=listing.get('roleTitles'),
        state_id=listing.get('stateId'),
        classification=get_classification(listing),
        sub_classification=get_sub_classification(listing),
        advertiser=get_advertiser(listing),
        location=get_location(listing),
        company=get_company(listing),
    )
