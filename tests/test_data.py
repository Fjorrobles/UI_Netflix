"""
Test the data module.
Author: Wolf Paulus (wolf@paulus.com) Modified by Fjor Robles
"""
from unittest import TestCase
from WS_NetflixMovies import web_scraper1
from os.path import exists, join
from os import remove


class Test(TestCase):
    def test_data_acquisition(self):
        """
            fetching new data and poking around a little
        """
        path_to_data_file = join("Users","fjorrobles","Desktop","Folder","UI_Netflix","app", "data", "movies.json")
        web_scraper1.clear()

        if exists(path_to_data_file):
            remove(path_to_data_file)
        assert False == exists(path_to_data_file)
        movies = web_scraper1()
        assert exists(path_to_data_file)