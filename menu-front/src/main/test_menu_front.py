import unittest
import utils.list

class TestMenuDelete(unittest.TestCase):

    def test_rewrite_ok(self):
        json = [{'id': 1, 'name': 'Menu spécial du chef2', 'dishes': [{'id': 1, 'name': 'Bananes aux fraises'}, {'id': 2, 'name': 'Bananes flambées le retour'}]}]
        text = utils.list.rewrite(json)
        self.assertEqual(text, '1 Menu spécial du chef2\n   Bananes aux fraises\n   Bananes flambées le retour\n')

    def test_rewrite_empty(self):
        json = []
        text = utils.list.rewrite(json)
        self.assertEqual(text,'There is no menu yet')

if __name__ == '__main__':
    unittest.main()