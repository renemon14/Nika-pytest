import unittest

from elements import Icd10DataMainPage
from functions.GeneralFunctions import GeneralFunctions
from assertpy import assert_that

class CheckSteps(unittest.TestCase, GeneralFunctions):


    def checkButtonInMenuBar(self, btn):
        self.implicit_wait_visible(Icd10DataMainPage.menuBar)
        elements = self.driver.find_elements(*Icd10DataMainPage.menuBar)
        x = len(elements)
        j = 1
        for i in elements:
            if btn in i.text:
                print("Button visible in Menu Bar")
                break
            elif x == j:
                raise ValueError("Button is not visible in Menu Bar")
            j += 1

    def checkDropDownMenuOpens(self, btn):
        self.implicit_wait_visible(Icd10DataMainPage.menuBar)
        element = self.driver.find_element(*Icd10DataMainPage.menuCodes)
        self.assertIn(element.text, btn)
        #assert_that(element.text).contains(btn)
        self.click_element(Icd10DataMainPage.menuCodes)
        self.implicit_wait_visible(Icd10DataMainPage.menuCodesOpen)


    def checkSearchFieldTopPage(self):
        self.implicit_wait_visible(Icd10DataMainPage.searchField)
        locationElement = self.driver.find_element(*Icd10DataMainPage.searchField).location
        self.assertLess(locationElement["y"], 50)
        #assert_that(locationElement["y"]).is_less_than(50)

    def checkSearchResults(self, result):
        self.implicit_wait_visible(Icd10DataMainPage.searchResults)
        elements = self.driver.find_elements(*Icd10DataMainPage.searchResults)
        x = len(elements)
        j = 1
        for i in elements:
            if result in i.text:
                print("Result found")
                print("Result " + str(j) + ":" + i.text)
                break
            elif x == j:
                raise ValueError("Result not found")
            j += 1