import allure
from pages.elements_page import TextBoxPage, CheckBoxPage


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
