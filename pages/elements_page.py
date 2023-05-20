import base64
import os

import allure
import random

import requests
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from generator.generator import generated_person, generated_file
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablePageLocators, ButtonsPageLocators, LinksPageLocators, ImageLinksPageLocators, LoadFilesPageLocators


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    @allure.step("Fill in all fields")
    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address.replace('\n', ' ')
        with allure.step('filing fields'):
            self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
            self.element_is_visible(self.locators.EMAIL).send_keys(email)
            self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
            self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        with allure.step('click submit button'):
            self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    @allure.step('check filled form')
    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    @allure.step('Opened full checkbox list')
    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    @allure.step('Click on random checkbox')
    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        count = 21
        while count != 0:
            item = item_list[random.randint(1, 15)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    @allure.step('Get list of checked checkboxes')
    def get_list_checked_checkboxes(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element('xpath', self.locators.TITLE_ITEM)
            data.append(title_item.text)
        return str(data).replace(' ', '').replace('doc', '').replace('.', '').lower()

    @allure.step('Get output result')
    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).replace(' ', '').lower()


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators

    @allure.step('Click on radio button')
    def click_on_radio_button(self, choice):
        choices = {
            'yes': self.locators.YES_RADIOBUTTON,
            'impressive': self.locators.IMPRESSIVE_RADIOBUTTON,
            'no': self.locators.NO_RADIOBUTTON,
        }
        self.element_is_visible(choices[choice]).click()

    @allure.step('Get output result')
    def get_output_result(self):
        return self.element_is_present(self.locators.OUTPUT_RESULT).text


class WebTablePage(BasePage):
    locators = WebTablePageLocators

    @allure.step('Add a new person')
    def add_new_person(self):
        count = 1
        while count != 0:
            person_info = next(generated_person())
            first_name = person_info.first_name
            last_name = person_info.last_name
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            self.element_is_visible(self.locators.ADD_BUTTON).click()
            self.element_is_visible(self.locators.FIRSTNAME_INPUT).send_keys(first_name)
            self.element_is_visible(self.locators.LASTNAME_INPUT).send_keys(last_name)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
            self.element_is_visible(self.locators.SUBMIT).click()
            count -= 1
            return [first_name, last_name, str(age), email, str(salary), department]

    @allure.step('Check added person')
    def check_added_person(self):
        people_list = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        data = []
        for item in people_list:
            data.append(item.text.splitlines())
        return data

    @allure.step('Find a person')
    def find_some_person(self, key_word):
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(key_word)

    @allure.step('Check founded person')
    def check_founded_person(self):
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        row = delete_button.find_element('xpath', self.locators.ROW_PARENT)
        return row.text.splitlines()

    @allure.step('Update person information')
    def update_person_info(self):
        person_info = next(generated_person())
        age = person_info.age
        self.element_is_visible(self.locators.UPDATE_BUTTON).click()
        self.element_is_visible(self.locators.AGE_INPUT).clear()
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
        self.element_is_visible(self.locators.SUBMIT).click()
        return str(age)

    @allure.step('Delete person')
    def delete_person(self):
        self.element_is_visible(self.locators.DELETE_BUTTON).click()

    @allure.step('Check that the person has been deleted')
    def check_deleted_person(self):
        return self.element_is_present(self.locators.NO_ROWS_FOUND).text

    @allure.step('Check rows count')
    def check_rows_count(self):
        list_rows = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        return len(list_rows)

    @allure.step('Select some rows')
    def select_some_rows(self):
        data = []
        count = [5, 10, 20, 25, 50, 100]
        for x in count:
            count_row_button = self.element_is_present(self.locators.COUNT_ROW_LIST)
            self.go_to_element(count_row_button)
            count_row_button.click()
            self.element_is_visible((By.CSS_SELECTOR, f'option[value="{x}"]')).click()
            data.append(self.check_rows_count())
        return data


class ButtonsPage(BasePage):
    locators = ButtonsPageLocators

    @allure.step('Check type of click')
    def check_click_type(self, element):
        return self.element_is_present(element).text

    @allure.step('Click on different type buttons')
    def click_on_dif_buttons(self, click_type):
        if click_type == 'double':
            self.action_double_click(self.element_is_visible(self.locators.DOUBLE_CLICK_BUTTON))
            return self.check_click_type(self.locators.SUCCESS_DOUBLE_CLICK)
        if click_type == 'right':
            self.action_right_click(self.element_is_visible(self.locators.RIGHT_CLICK_BUTTON))
            return self.check_click_type(self.locators.SUCCESS_RIGHT_CLICK)
        if click_type == 'click':
            self.element_is_visible(self.locators.CLICK_BUTTON).click()
            return self.check_click_type(self.locators.SUCCESS_CLICK)


class LinksPage(BasePage):
    locators = LinksPageLocators

    @allure.step('Check new tab simple link')
    def check_new_tab_link(self, choice):
        choices = {
            'simple_link': self.locators.SIMPLE_LINK,
            'dynamic_link': self.locators.DYNAMIC_LINK
        }
        link = self.element_is_visible(choices[choice])
        link_href = link.get_attribute('href')
        request = requests.get(link_href)
        if request.status_code == 200:
            link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.driver.current_url
            return link_href, url
        else:
            return link_href, request.status_code

    @allure.step('Check bad request link')
    def check_link_api_call(self, url, choice):
        choices = {
            'created_link': self.locators.CREATED_LINK,
            'no_content_link': self.locators.NO_CONTENT_LINK,
            'moved_link': self.locators.MOVED_LINK,
            'bad_request_link': self.locators.BAD_REQUEST_LINK,
            'unauthorized_link': self.locators.UNAUTHORIZED_LINK,
            'forbidden_link': self.locators.FORBIDDEN_LINK,
            'not_found_link': self.locators.NOT_FOUND_LINK
        }
        request = requests.get(url)
        if request.status_code == 200:
            self.element_is_present(choices[choice]).click()
        else:
            return request.status_code


class ImageLinksPage(BasePage):
    locators = ImageLinksPageLocators

    @allure.step('Check correct image link')
    def check_correct_image_link(self):
        pass


class LoadFilesPage(BasePage):
    locators = LoadFilesPageLocators

    @allure.step('Upload file')
    def upload_file(self):
        file_name, path = generated_file()
        self.element_is_present(self.locators.UPLOAD_FILE).send_keys(path)
        os.remove(path)
        result = self.element_is_present(self.locators.UPLOADED_RESULT).text
        return file_name.split('/')[-1], result.split('\\')[-1]

    @allure.step('Download file')
    def download_file(self):
        link_1 = self.element_is_present(self.locators.DOWNLOAD_FILE).get_attribute('href')
        link_2 = base64.b64decode(link_1)
        path = rf'/Users/timur/PycharmProjects/demoqa_autotests/test_file_{random.randint(0, 999)}.jpg'
        with open(path, 'wb+') as f:
            offset = link_2.find(b'\xff\xd8')
            f.write(link_2[offset:])
            check_file = os.path.exists(path)
            f.close()
        os.remove(path)
        return check_file
