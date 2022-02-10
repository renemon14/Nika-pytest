from elements import Icd10DataMainPage
from functions.GeneralFunctions import GeneralFunctions



class GeneralSteps(GeneralFunctions):


    def searchCode(self, code):
        self.implicit_wait_visible(Icd10DataMainPage.searchField)
        self.send_key(Icd10DataMainPage.searchField, code)
        self.click_element(Icd10DataMainPage.btnSearch)