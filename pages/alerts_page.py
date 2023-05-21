import random
import time

import allure

from locators.alerts_page_locators import BrowserWindowsPageLocators, AlertsPageLocators, FramesPageLocators, \
    NestedFramesPageLocators, ModalDialogsPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    @allure.step('Check opened new tab')
    def check_open_new_tab(self):
        self.element_is_visible(self.locators.NEW_TAB).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        title_text = self.element_is_visible(self.locators.NEW_TITLE).text
        return title_text

    @allure.step('Check opened new window')
    def check_open_new_window(self):
        self.element_is_visible(self.locators.NEW_WINDOW).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        title_text = self.element_is_visible(self.locators.NEW_TITLE).text
        return title_text


class AlertsPage(BasePage):
    locators = AlertsPageLocators()

    @allure.step('Get text from alert')
    def check_alert(self):
        self.element_is_visible(self.locators.ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    @allure.step('Check alert appear after 5 seconds')
    def check_appear_alert_5_sec(self):
        self.element_is_visible(self.locators.ALERT_AFTER_FIVE_SECONDS).click()
        time.sleep(6)
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    @allure.step('Check confirm alert')
    def check_confirm_alert(self):
        self.element_is_visible(self.locators.CONFIRM_ALERT).click()
        alert_window = self.driver.switch_to.alert
        alert_window.accept()
        result = self.element_is_visible(self.locators.CONFIRM_RESULT).text
        return result

    @allure.step('Check prompt alert')
    def check_prompt_alert(self):
        test = f'{random.randint(1, 100)}'
        self.element_is_visible(self.locators.PROMPT_ALERT).click()
        alert_window = self.driver.switch_to.alert
        alert_window.send_keys(test)
        alert_window.accept()
        result = self.element_is_visible(self.locators.PROMPT_RESULT).text
        return result, test


class FramesPage(BasePage):
    locators = FramesPageLocators()

    @allure.step('Check frame')
    def check_frame(self, frame):
        if frame == 'frame1':
            frame = self.element_is_present(self.locators.FIRST_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            frame_title = self.element_is_present(self.locators.TITLE_FRAME).text
            self.driver.switch_to.default_content()
            return [frame_title, width, height]
        if frame == 'frame2':
            frame = self.element_is_present(self.locators.SECOND_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            frame_title = self.element_is_present(self.locators.TITLE_FRAME).text
            self.driver.switch_to.default_content()
            return [frame_title, width, height]


class NestedFramesPage(BasePage):
    locators = NestedFramesPageLocators()

    @allure.step('Check nested frame')
    def check_nested_frame(self):
        parent_frame = self.element_is_present(self.locators.PARENT_FRAME)
        self.driver.switch_to.frame(parent_frame)
        parent_text = self.element_is_present(self.locators.PARENT_TEXT).text
        child_frame = self.element_is_present(self.locators.CHILD_FRAME)
        self.driver.switch_to.frame(child_frame)
        child_text = self.element_is_present(self.locators.CHILD_TEXT).text
        return parent_text, child_text


class ModalDialogsPage(BasePage):
    locators = ModalDialogsPageLocators()

    @allure.step('Check modal dialogs')
    def check_modal_dialogs(self):
        self.element_is_visible(self.locators.SMALL_MODAL_BUTTON).click()
        small_title = self.element_is_visible(self.locators.SMALL_MODAL_TITLE).text
        small_body = self.element_is_visible(self.locators.SMALL_MODAL_BODY).text
        self.element_is_visible(self.locators.SMALL_MODAL_CLOSE_BUTTON).click()
        self.element_is_visible(self.locators.LARGE_MODAL_BUTTON).click()
        large_title = self.element_is_visible(self.locators.LARGE_MODAL_TITLE).text
        large_body = self.element_is_visible(self.locators.LARGE_MODAL_BODY).text
        self.element_is_visible(self.locators.LARGE_MODAL_CLOSE_BUTTON).click()
        return [small_title, len(small_body)], [large_title, len(large_body)]