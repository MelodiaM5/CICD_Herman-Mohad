# Standard library imports...
try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

# Third-party imports...
import requests

# Local imports...
from services.constants import BASE_URL



def get_todos():
    response = requests.get(BASE_URL)
    if response.ok:
        return response
    else:
        return None