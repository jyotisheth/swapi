import unittest
from api_helper import ApiHelper

class ApiHelperTest(unittest.TestCase):

    def setUp(self):
        self.api_helper = ApiHelper()

    def tearDown(self):
        pass

    def test_get_all_star_wars_characters(self):
        """
        This test goes through each people pages @ https://swapi.co/api/people/
        and verifies non empty array is returned.
        """
        starwars_characters = self.api_helper.star_wars_characters()
        self.assertTrue(starwars_characters!=[])

    def test_get_star_wars_characters_by_page(self):
        """
        This test gets response of given specific page @ https://swapi.co/api/people/
        and verifies non empty array is returned.
        """
        starwars_characters = self.api_helper.star_wars_characters(2)
        self.assertTrue(starwars_characters!=[])
