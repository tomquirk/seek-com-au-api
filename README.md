# seek-com-au-api

🧑‍💼 Python wrapper for the seek.com.au API <small>(unofficial)</small>

## Installation

Using **Python >= 3.6**:

```bash
pip install -e git+https://github.com/tomquirk/seek-com-au-api.git#egg=seek_com_au_api
```

### Example usage

```python
from seek_com_au import SeekComAu

api = SeekComAu()

# Search job listings
listings = api.search(keywords='public health officer', limit=5)

# Get listing
listing = api.get_listing(listings[0].id)
```

## Data classes

### [Listing](/seek_com_au/objects/listing.py#L6)

Data class for a listing. See [listing.py](/seek_com_au/objects/listing.py#L6) for reference.
