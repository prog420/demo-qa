from selenium.webdriver.common.by import By

from app.ui.base.base_page_locators import BasePageLocators


class PracticeFormPageLocators(BasePageLocators):
    first_name = (By.CSS_SELECTOR, 'input#firstName')
    last_name = (By.XPATH, '//input[@id="lastName"]')
    email = (By.ID, 'userEmail')
    gender = (By.CSS_SELECTOR, 'div#genterWrapper label[for="gender-radio-{}"]')
    phone = (By.CSS_SELECTOR, 'input#userNumber')
    date_of_birth = (By.CSS_SELECTOR, 'input#dateOfBirthInput')
    date_of_birth_year = (By.CSS_SELECTOR, 'select.react-datepicker__year-select')
    date_of_birth_month = (By.CSS_SELECTOR, 'select.react-datepicker__month-select')
    # Some days can be found 2 times (e.g. August 2024, 28 - 2 elements, one from July, one from August)
    date_of_birth_day = (By.CSS_SELECTOR, 'div.react-datepicker__day--{}:not(.react-datepicker__day--outside-month)')
    subjects = (By.CSS_SELECTOR, 'input#subjectsInput')
    hobby = (By.CSS_SELECTOR, 'div#hobbiesWrapper label[for="hobbies-checkbox-{}"')
    picture = (By.CSS_SELECTOR, 'input#uploadPicture')
    curr_address = (By.CSS_SELECTOR, 'textarea#currentAddress')
    state = (By.CSS_SELECTOR, 'div#state')
    state_option = (
        By.XPATH, '//div[@id="stateCity-wrapper"]//div[contains(@id, "react-select-3-option") and text()="{}"]'
    )
    city = (By.CSS_SELECTOR, 'div#city')
    city_option = (
        By.XPATH, '//div[@id="stateCity-wrapper"]//div[contains(@id, "react-select-4-option") and text() ="{}"]'
    )
    submit_form_btn = (By.CSS_SELECTOR, 'button#submit')
    # Submitted Form Results
    modal_title = (By.CSS_SELECTOR, 'div.modal-title')
    table_value = (By.XPATH, '//tr[td[text()="{}"]]//td[2]')
