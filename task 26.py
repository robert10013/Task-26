from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class IMDBSearchPage:
    def _init_(self, driver):
        self.driver = driver
        self.url = "https://www.imdb.com/search/name/"
        self.name_input_locator = (By.ID, "name")
        self.birth_month_dropdown_locator = (By.ID, "birth_month")
        self.birth_year_input_locator = (By.ID, "birth_year")
        self.birth_place_input_locator = (By.ID, "birth_place")
        self.role_dropdown_locator = (By.ID, "roles")
        self.search_button_locator = (By.XPATH, "//button[text()='Search']")

    def open(self):
        self.driver.get(self.url)

    def enter_name(self, name):
        name_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.name_input_locator)
        )
        name_input.send_keys(name)

    def select_birth_month(self, month):
        birth_month_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.birth_month_dropdown_locator)
        )
        select_birth_month = Select(birth_month_dropdown)
        select_birth_month.select_by_visible_text(month)

    def enter_birth_year(self, year):
        birth_year_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.birth_year_input_locator)
        )
        birth_year_input.send_keys(year)

    def enter_birth_place(self, place):
        birth_place_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.birth_place_input_locator)
        )
        birth_place_input.send_keys(place)

    def select_role(self, role):
        role_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.role_dropdown_locator)
        )
        select_role = Select(role_dropdown)
        select_role.select_by_visible_text(role)

    def click_search(self):
        search_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.search_button_locator)
        )
        search_button.click()