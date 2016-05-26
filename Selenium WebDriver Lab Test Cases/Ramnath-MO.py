# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import unittest, time, re


class ALinks(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://deanza.edu/"
        self.verificationErrors = []

    def test_a_links(self):
        link_title = {
            "Music Department": "De Anza College :: Music :: Home",
            "MyPortal Login Password": "De Anza College :: Registration :: MyPortal Password",
            "News": "De Anza College :: @ De Anza :: News and Notices Home",
            "Nursing": "De Anza College :: Nursing Department :: Home",
            "Occupational Training Institute": "De Anza College :: Occupational Training Institute :: Home",
            "OmniUpdate": "De Anza College :: Web Publishing Guide :: OmniUpdate at De Anza",
            "Online Education": "De Anza College :: Online Education :: Home",
            "Online Services": "De Anza College :: Registration :: De Anza Admissions and MyPortal Registration"
        }

        driver = self.driver
        driver.get(self.base_url + "directory/dir-az.html")

        for link in link_title:
            title = link_title[link]
            driver.find_element_by_link_text(link).click()
            try:
                self.assertEqual(title, driver.title)
            except AssertionError as e:
                self.verificationErrors.append(str(e))
            driver.back()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
