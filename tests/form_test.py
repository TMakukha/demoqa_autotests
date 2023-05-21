import time

import allure

from pages.form_page import FormPage


@allure.suite('Form')
class TestForm:

    @allure.feature('FormPage')
    class TestFormPage:

        @allure.title('Form filling test')
        def test_form_field(self, driver):
            form_page = FormPage(driver, 'https://demoqa.com/automation-practice-form')
            form_page.open()
            first_name, last_name, email = form_page.fill_form_fields()
            result = form_page.form_result()
            assert f'{first_name} {last_name}' == result[0], "The field was filled incorrectly or wasn't filled"
            assert f'{email}' == result[1], "The field was filled incorrectly or wasn't filled"
