# Third-party imports...
from nose.tools import assert_is_not_none

# Local imports...
from services.list import listmenus

def test_request_response():
    # Call the service, which will send a request to the server.
    response = listmenus('https://menu-server-theo.herokuapp.com/menus')

    # If the request is sent successfully, then I expect a response to be returned.
    assert_is_not_none(response)
