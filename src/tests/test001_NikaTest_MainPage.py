import unittest

import os
from dotenv import load_dotenv
from elements import Icd10DataMainPage
from functions.GeneralFunctions import GeneralFunctions
from tests.steps.CheckSteps import CheckSteps
from tests.steps.GeneralSteps import GeneralSteps



class Test001_NikaTest_MainPage(unittest.TestCase, GeneralFunctions):

    def setUp(self):
        load_dotenv()
        self.open_browser(os.getenv("URLNIKATEST"), "Chrome")

    def test_NikaMainPage(self):
        self.implicit_wait_present(Icd10DataMainPage.logo)
        CheckSteps.checkButtonInMenuBar(self, "Codes")
        CheckSteps.checkDropDownMenuOpens(self, "Codes")
        CheckSteps.checkSearchFieldTopPage(self)
        GeneralSteps.searchCode(self, "Covid-19")
        CheckSteps.checkSearchResults(self, "COVID-19")


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
