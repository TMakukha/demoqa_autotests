import allure

from locators.alerts_page_locators import BrowserWindowsPageLocators, AlertsPageLocators, FramesPageLocators, \
    NestedFramesPageLocators, ModalDialogsPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    @allure.step('Check opened new tab')
    def check_open_new_tab(self):
        pass

    @allure.step('Check opened new window')
    def check_open_new_window(self):
        pass


class AlertsPage(BasePage):
    locators = AlertsPageLocators()

    @allure.step('Get text from alert')
    def get_text_from_alert(self):
        pass

    @allure.step('Check alert appear after 5 seconds')
    def check_appear_alert_5_sec(self):
        pass

    @allure.step('Check confirm alert')
    def check_confirm_alert(self):
        pass

    @allure.step('Check prompt alert')
    def check_prompt_alert(self):
        pass


class FramesPage(BasePage):
    locators = FramesPageLocators

    @allure.step('Check frame')
    def check_frame(self):
        pass


class NestedFramesPage(BasePage):
    locators = NestedFramesPageLocators

    @allure.step('Check nested frame')
    def check_nested_frame(self):
        pass


class ModalDialogsPage(BasePage):
    locators = ModalDialogsPageLocators

    @allure.step('Check modal dialogs')
    def check_modal_dialogs(self):
        pass
