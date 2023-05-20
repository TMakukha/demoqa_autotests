import random

import allure
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage, \
    LoadFilesPage


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
        def test_web_table_add_new_person(self, driver):
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
            # to successfully pass the test, you need to disable the footer
            # web_table_page.remove_footer()
            count = web_table_page.select_some_rows()
            assert count == [5, 10, 20, 25, 50,
                             100], 'The number of rows in the table has not been changed or has changed incorrectly'

    @allure.feature('Test buttons')
    class TestButtons:

        @allure.title('Check different clicks on the buttons')
        def test_different_clicks_on_buttons(self, driver):
            buttons_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            buttons_page.open()
            click = buttons_page.click_on_dif_buttons('click')
            double_click = buttons_page.click_on_dif_buttons('double')
            right_click = buttons_page.click_on_dif_buttons('right')
            assert click == "You have done a dynamic click", "The dynamic click button was not pressed"
            assert double_click == "You have done a double click", "The double click button was not pressed"
            assert right_click == "You have done a right click", "The right click button was not pressed"

    @allure.feature('Test links')
    class TestLinksPage:
        @allure.title('Checking the simple link')
        def test_check_simple_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            href_link, current_url = links_page.check_new_tab_link('simple_link')
            assert href_link == current_url, "the link is broken or url is incorrect"

        @allure.title('Checking the dynamic link')
        def test_check_dynamic_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            href_link, current_url = links_page.check_new_tab_link('dynamic_link')
            assert href_link == current_url, "the link is broken or url is incorrect"

        @allure.title('Checking the created link')
        def test_created_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_link_api_call('https://demoqa.com/created', 'created_link')
            assert response_code == 201, "the link works or the status code in son 400"

        @allure.title('Checking the no content link')
        def test_no_content_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_link_api_call('https://demoqa.com/no-content', 'content_link')
            assert response_code == 204, "the link works or the status code in son 400"

        @allure.title('Checking the moved link')
        def test_moved_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_link_api_call('https://demoqa.com/moved', 'moved_link')
            assert response_code == 301, "the link works or the status code in son 400"

        @allure.title('Checking the bad request link')
        def test_bad_request_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_link_api_call('https://demoqa.com/bad-request', 'bad_request_link')
            assert response_code == 400, "the link works or the status code in son 400"

        @allure.title('Checking the unauthorized link')
        def test_unauthorized_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_link_api_call('https://demoqa.com/unauthorized', 'unauthorized_link')
            assert response_code == 401, "the link works or the status code in son 400"

        @allure.title('Checking the forbidden link')
        def test_forbidden_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_link_api_call('https://demoqa.com/forbidden', 'forbidden_link')
            assert response_code == 403, "the link works or the status code in son 400"

        @allure.title('Checking the not found link')
        def test_not_found_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_link_api_call('https://demoqa.com/invalid-url', 'not_found_link')
            assert response_code == 404, "the link works or the status code in son 400"

    @allure.feature('Test image links')
    class TestImageLinks:
        pass

    @allure.feature('Test load buttons')
    class TestLoadButtons:

        @allure.title('Uploading file check')
        def test_upload_file(self, driver):
            load_page = LoadFilesPage(driver, 'https://demoqa.com/upload-download')
            load_page.open()
            load_page.upload_file()
            file_name, result = load_page.upload_file()
            assert file_name == result, "The file wasn't loaded"

        @allure.title('Downloading file check')
        def test_download_file(self, driver):
            load_page = LoadFilesPage(driver, 'https://demoqa.com/upload-download')
            load_page.open()
            check = load_page.download_file()
            assert check is True, "The file wasn't downloaded"
