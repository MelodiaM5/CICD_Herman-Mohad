# Third-party imports...
from nose.tools import assert_is_not_none

# Local imports...
from services.list import listmenus
from constants import BASE_URL

def test_request_response():
    # Call the service, which will send a request to the server.
    response = listmenus(BASE_URL)

    # If the request is sent successfully, then I expect a response to be returned.
    assert_is_not_none(response)
