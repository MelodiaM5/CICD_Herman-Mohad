# Third-party imports...
from nose.tools import assert_is_not_none
import unittest
# Local imports...
from services.list import listmenus
from services.list import rewrite

def test_request_response():
    # Call the service, which will send a request to the server.
    response = listmenus('https://menu-server-theo.herokuapp.com/menus')

    # If the request is sent successfully, then I expect a response to be returned.
    assert_is_not_none(response)

    def test_rewrite_ok(self):
        json = [{'id': 1, 'name': 'Menu spécial du chef2', 'dishes': [{'id': 1, 'name': 'Bananes aux fraises'}, {'id': 2, 'name': 'Bananes flambées le retour'}]}]
        text = rewrite(json)
        self.assertEqual(text, '1 Menu spécial du chef2\n   Bananes aux fraises\n   Bananes flambées le retour\n')

    def test_rewrite_empty(self):
        json = []
        text = rewrite(json)
        self.assertEqual(text,'There is no menu yet')