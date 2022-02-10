from selenium.webdriver.common.by import By

logo = (By.CSS_SELECTOR, "div.navbar-header > a > img[src='/images/ICD10Data.com266x45.png']")
menuBar = (By.CSS_SELECTOR, "ul#navMenu > li")
menuCodes = (By.CSS_SELECTOR, "ul#navMenu > li:nth-child(1)")
menuCodesOpen = (By.CSS_SELECTOR, "ul#navMenu > li.dropdown.open:nth-child(1)")
searchField = (By.CSS_SELECTOR, "input#searchText")
btnSearch = (By.CSS_SELECTOR, "button#search")
searchResults = (By.CSS_SELECTOR, "div.searchLine")