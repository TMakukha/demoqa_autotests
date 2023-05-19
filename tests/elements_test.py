import random

import allure
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage


@allure.suite("Elements")
class TestElements:
    @allure.feature('TextBox')
    class TestTextBox:

        @allure.title('Check TextBox')
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_cur_addr, output_per_addr = text_box_page.check_filled_form()
            assert full_name == output_name, "the full name does not match"
            assert email == output_email, "the email does not match"
            assert current_address == output_cur_addr, "the current address does not match"
            assert permanent_address == output_per_addr, "the permanent address does not match"

    @allure.feature('CheckBox')
    class TestCheckBox:

        @allure.title('Check CheckBox')
        def test_checkbox(self, driver):
            checkbox_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            checkbox_page.open()
            checkbox_page.open_full_list()
            checkbox_page.click_random_checkbox()
            input_checkbox = checkbox_page.get_list_checked_checkboxes()
            output_checkbox = checkbox_page.get_output_result()
            assert input_checkbox == output_checkbox, "Checkboxes wasn't selected"

    @allure.feature('Radio button')
    class TestRadioButtons:

        @allure.title('Check radio buttons')
        def test_radio_buttons(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_on_radio_button("yes")
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_on_radio_button('impressive')
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.click_on_radio_button('no')
            output_no = radio_button_page.get_output_result()
            assert output_yes == 'Yes', "'YES' wasn't selected"
            assert output_impressive == 'Impressive', "'Impressive' wasn't selected"
            assert output_no == 'No', "'No' wasn't selected"

    @allure.feature('Web table')
    class TestWebTable:

        @allure.title('Add a new person to web table')
        def test_webtable_add_new_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            result = web_table_page.check_added_person()
            assert new_person in result, "The person hasn't been added"

        @allure.title('Found person in the table')
        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            key_word = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.find_some_person(key_word)
            table_result = web_table_page.check_founded_person()
            assert key_word in table_result, "The person hasn't found in table"

        @allure.title('Checking to update the persons info in the table')
        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            lastname = web_table_page.add_new_person()[1]
            web_table_page.find_some_person(lastname)
            age = web_table_page.update_person_info()
            row = web_table_page.check_founded_person()
            assert age in row, "The person data has not been changed"

        @allure.title('Checking to remove a person from the table')
        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            web_table_page.find_some_person(email)
            web_table_page.delete_person()
            text = web_table_page.check_deleted_person()
            assert text == "No rows found", "Person hasn't been deleted"

        @allure.title('Check the change in the number of rows in the table')
        def test_web_table_change_count_row(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            web_table_page.remove_footer()
            count = web_table_page.select_some_rows()
            assert count == [5, 10, 20, 25, 50,
                             100], 'The number of rows in the table has not been changed or has changed incorrectly'
