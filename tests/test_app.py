"""
Test the app module.
Author: Wolf Paulus (wolf@paulus.com) Modified by Fjor Robles
"""
from unittest import TestCase
from streamlit.testing.v1 import AppTest


class Test(TestCase):    
    def test_ui_title_and_header(self):
        """
        find out more about how to test streamlit apps:
        https://docs.streamlit.io/library/api-reference/app-testing
        """
        at = AppTest.from_file("/Users/fjorrobles/Desktop/Folder/UI_Netflix/app/mainpage.py")
        at.run()

        assert at.title[0].value.startswith("Netflix")
        assert not at.exception
