from pages.base_page import BasePage
from selenium import webdriver


class DiagnosticsPage(BasePage):
    # тест жестко завязан на конкретную систему, когда бэк будет готов убрать привязку
    # дописать когда появяться id в полях
    def change_system(self, browser: webdriver.Chrome):
        # tab system and component
        pass




        # select_system = self.browser.find_element(*DiagnosticPageLocator.CHOICE_SYSTEM_LIST)
        # select_system.click()
        # choice_system = self.browser.find_element(*DiagnosticPageLocator.CHOICE_SYSTEM_ITEM)
        # choice_system.click()
        # choice_system = self.browser.find_elements(*DiagnosticPageLocator.CHOICED_SYSTEM_TEXT)[0].text
        # select_component = self.browser.find_element(*DiagnosticPageLocator.CHOICE_COMPONENT_LIST)
        # select_component.click()
        # choice_component = self.browser.find_element(*DiagnosticPageLocator.CHOISE_COMPONENT_ITEM)
        # choice_component.click()
        # choice_component_text = (self.browser.find_elements(*DiagnosticPageLocator.CHOICED_SYSTEM_TEXT)[2].text)
        # assert choice_system == 'System1', 'Wrong choiced System text'
        # assert choice_component_text == 'Диагностика ходовой', 'Wrong chiced component text'
        # button_continue = self.browser.find_element(*DiagnosticPageLocator.DIAGNOSTIC_BUTTON)
        # button_continue.click()
        # date_time_title = self.browser.find_element(*DiagnosticPageLocator.SUB_TITLE_DIAGNOSTIC).text
        # assert date_time_title == 'Укажите удобные для вас дату и время', 'Wrong transition to tab data and time'
        #
        # #tab date and time
        # current_date = int(date.today().strftime('%d'))
        # choice_day = self.browser.find_elements(*DiagnosticPageLocator.CALENDAR_DAY)[current_date - 1]
        # choice_day.click()
        # time_list = self.browser.find_element(By.CSS_SELECTOR, 'label[for="12:00-4"]')
        # time_list.click()
        # diagnostic_button_date = WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((DiagnosticPageLocator.DIAGNOSTIC_BUTTON_DATE)))
        # diagnostic_button_date.click()
        # sub_title_choice_auto = self.browser.find_element(*DiagnosticPageLocator.SUB_TITLE_DIAGNOSTIC).text
        # assert sub_title_choice_auto == 'Выберите автомобиль,требующий диагностики', 'wrong transition to tab choice your auto'


