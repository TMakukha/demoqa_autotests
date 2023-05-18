import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    @allure.step('Browser opening')
    def open(self):
        self.driver.get(self.url)

    @allure.step('Find visible element')
    def element_is_visible(self, locator, timeout=2):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('Find invisible element')
    def element_is_not_visible(self, locator, timeout=2):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    @allure.step('Find visible elements')
    def elements_are_visible(self, locator, timeout=2):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    @allure.step('Find present element')
    def element_is_present(self, locator, timeout=2):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    @allure.step('Find present elements')
    def elements_are_present(self, locator, timeout=2):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    @allure.step('Find clickable element')
    def element_is_clickable(self, locator, timeout=2):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step('Go to element')
    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

