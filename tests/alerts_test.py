import allure

from pages.alerts_page import BrowserWindowsPage, AlertsPage, FramesPage, NestedFramesPage, ModalDialogsPage


@allure.suite('Test alerts frames and windows')
class TestAlertsFrameWindows:
    @allure.feature('Browser Windows')
    class TestBrowserWindows:

        @allure.title('Checking the opening new tab')
        def test_new_tab(self, driver):
            browser_windows_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            browser_windows_page.open()
            result = browser_windows_page.check_open_new_tab()
            assert result == 'This is a sample page'

        @allure.title('Checking the opening new window')
        def test_new_window(self, driver):
            browser_windows_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            browser_windows_page.open()
            result = browser_windows_page.check_open_new_window()
            assert result == 'This is a sample page'

    @allure.feature('Alerts page')
    class TestAlertsPage:
        @allure.title('Checking opened alert')
        def test_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_alert()
            assert alert_text == 'You clicked a button'

        @allure.title('Checking alert that opened after 5 seconds')
        def test_alert_five_seconds(self, driver):
            alert_five_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_five_page.open()
            alert_text = alert_five_page.check_appear_alert_5_sec()
            assert alert_text == 'This alert appeared after 5 seconds'

        @allure.title('Checking alert with confirm button')
        def test_confirm_alert(self, driver):
            confirm_alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            confirm_alert_page.open()
            alert_text = confirm_alert_page.check_confirm_alert()
            assert alert_text == 'You selected Ok'

        @allure.title('Check prompt alert')
        def test_prompt_alert(self, driver):
            prompt_alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            prompt_alert_page.open()
            result, alert_text = prompt_alert_page.check_prompt_alert()
            assert alert_text in result

    @allure.feature('Frame page')
    class TestFramePage:
        @allure.title('Check page frames')
        def test_page_frames(self, driver):
            frames_page = FramesPage(driver, 'https://demoqa.com/frames')
            frames_page.open()
            frame_result_1 = frames_page.check_frame('frame1')
            frame_result_2 = frames_page.check_frame('frame2')
            assert frame_result_1 == ['This is a sample page', '500px', '350px']
            assert frame_result_2 == ['This is a sample page', '100px', '100px']

    @allure.feature('Nested frames page')
    class TestNestedFrames:
        @allure.title('Check page with nested frames')
        def test_nested_frames(self, driver):
            nested_frames_page = NestedFramesPage(driver, 'https://demoqa.com/nestedframes')
            nested_frames_page.open()
            parent_frame, child_frame = nested_frames_page.check_nested_frame()
            assert parent_frame == 'Parent frame'
            assert child_frame == 'Child Iframe'

    @allure.feature('Modal Dialog Page')
    class TestModalDialog:
        @allure.title('Check page with modal dialogs')
        def test_modal_dialogs(self, driver):
            modal_dialog_page = ModalDialogsPage(driver, 'https://demoqa.com/modal-dialogs')
            modal_dialog_page.open()
            small, large = modal_dialog_page.check_modal_dialogs()
            assert small[1] < large[1], "Text in large dialog is less than text in small dialog"
            assert small[0] == 'Small Modal', "Title in small dialog is not 'Small Modal'"
            assert large[0] == 'Large Modal', "Title in large dialog is not 'Large Modal'"
