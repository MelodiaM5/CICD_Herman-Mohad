# Third-party imports...
from nose.tools import assert_is_not_none

# Local imports...
from services.delete import delete


def test_request_response():

    # there is no menus id 0 but we just want to see if our function make a connection with the servor
    SUP_URL = 'https://menu-server-theo.herokuapp.com'
    # Call the service, which will send a request to the server.
    response = delete(SUP_URL,'0')

    # If the request is sent successfully, then I expect a response to be returned.
    assert_is_not_none(response)
