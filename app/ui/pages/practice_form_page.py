import datetime
from typing import List, Text

import allure
from assertpy import assert_that, soft_assertions
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import Select

from app.routes import Routes
from app.ui.base.base_page import BasePage
from app.ui.pages.practice_form_page_locators import PracticeFormPageLocators
from data.registration_form.enums import Gender, Hobby
from data.registration_form.user import User


class PracticeFormPage(BasePage):
    url = Routes.PRACTICE_FORM
    locators = PracticeFormPageLocators()

    # region ACTIONS
    @allure.step("Enter First Name: {first_name}")
    def enter_first_name(self, first_name: Text):
        field = self.find_element(self.locators.first_name)
        field.clear()
        field.send_keys(first_name)

    @allure.step("Enter Last Name: {last_name}")
    def enter_last_name(self, last_name: Text):
        field = self.find_element(self.locators.last_name)
        field.clear()
        field.send_keys(last_name)

    @allure.step("Enter Email: {email}")
    def enter_email(self, email: Text):
        field = self.find_element(self.locators.email)
        field.clear()
        field.send_keys(email)

    @allure.step("Select Gender: {gender}")
    def select_gender(self, gender: Gender):
        locator = (self.locators.gender[0], self.locators.gender[1].format(gender.value))
        self.find_element(locator).click()

    @allure.step("Enter Phone Number: {phone_number}")
    def enter_phone_number(self, phone_number: Text):
        field = self.find_element(self.locators.phone)
        field.clear()
        field.send_keys(phone_number)

    @allure.step("Select Date of Birth: {date_of_birth}")
    def enter_date_of_birth(self, date_of_birth: datetime.date):
        # Convert date to "07-August-2024" format and split it
        day, month, year = date_of_birth.strftime('%d-%B-%Y').split("-")
        # Add padding to the day ("7" -> "007", "28" -> "028")
        day_padded = day.zfill(3)
        # Open datepicker
        datepicker = self.find_element(self.locators.date_of_birth)
        datepicker.click()
        # Handle year
        datepicker_year = Select(self.find_element(self.locators.date_of_birth_year))
        datepicker_year.select_by_value(year)
        # Handle month
        datepicker_month = Select(self.find_element(self.locators.date_of_birth_month))
        datepicker_month.select_by_visible_text(month)
        # Handle day
        datepicker_day_locator = (
            self.locators.date_of_birth_day[0], self.locators.date_of_birth_day[1].format(day_padded)
        )
        datepicker_day = self.find_element(datepicker_day_locator)
        datepicker_day.click()

    @allure.step("Enter Subjects: {subjects}")
    def enter_subjects(self, subjects: List[Text]):
        field = self.find_element(self.locators.subjects)
        field.clear()
        for subject in subjects:
            field.send_keys(subject)
            field.send_keys(Keys.ENTER)

    @allure.step("Select Hobbies: {hobbies}")
    def select_hobbies(self, hobbies: List[Hobby]):
        for hobby in hobbies:
            locator = (self.locators.hobby[0], self.locators.hobby[1].format(hobby.value))
            self.find_element(locator).click()

    @allure.step("Attach Picture")
    def attach_picture(self, path: Text):
        field = self.find_element(self.locators.picture)
        field.send_keys(path)

    @allure.step("Enter Address: {address}")
    def enter_address(self, address: Text):
        field = self.find_element(self.locators.curr_address)
        field.clear()
        field.send_keys(address)

    @allure.step("Select State: {state}")
    def select_state(self, state: Text):
        states = self.find_element(self.locators.state)
        self.scroll_element_into_view(states)
        states.click()
        state_option = self.find_element((self.locators.state_option[0], self.locators.state_option[1].format(state)))
        state_option.click()

    @allure.step("Select City: {city}")
    def select_city(self, city: Text):
        cities = self.find_element(self.locators.city)
        self.scroll_element_into_view(cities)
        cities.click()
        city_option = self.find_element((self.locators.city_option[0], self.locators.city_option[1].format(city)))
        city_option.click()

    @allure.step("Fill Form")
    def fill_form(self, user: User):
        """
        Facade method for filling registration form.
        :param user: dataclass with all required parameters.
        """
        self.enter_first_name(user.first_name)
        self.enter_last_name(user.last_name)
        self.enter_email(user.email)
        self.select_gender(user.gender)
        self.enter_phone_number(user.phone_number)
        self.enter_date_of_birth(user.date_of_birth)
        self.enter_subjects(user.subjects)
        self.select_hobbies(user.hobbies)
        self.attach_picture(user.picture)
        self.enter_address(user.address)
        self.select_state(user.state)
        self.select_city(user.city)

    @allure.step("Submit Form")
    def submit_form(self):
        self.find_element(self.locators.submit_form_btn).click()

    # endregion

    # region ASSERTIONS
    @allure.step("Assert that window Title is {expected_title}")
    def assert_modal_title_equal_to(self, expected_title):
        actual_title = self.find_element(self.locators.modal_title).text
        with soft_assertions():
            assert_that(actual_title, "Modal Window Title").is_equal_to(expected_title)

    @allure.step("Assert that saved User Data is Correct")
    def assert_saved_data_matches_user(self, user: User):
        with soft_assertions():
            self.assert_table_row_contains_value("Student Name", f"{user.first_name} {user.last_name}")
            self.assert_table_row_contains_value("Student Email", user.email)
            self.assert_table_row_contains_value("Gender", user.gender)
            self.assert_table_row_contains_value("Mobile", user.phone_number)
            self.assert_table_row_contains_value("Date of Birth", user.date_of_birth.strftime('%d %B,%Y'))
            self.assert_table_row_contains_value("Subjects", ", ".join(user.subjects))
            self.assert_table_row_contains_value("Hobbies", ", ".join(map(str, user.hobbies)))
            self.assert_table_row_contains_value("Address", user.address)

    def assert_table_row_contains_value(self, row, expected_value):
        locator = (self.locators.table_value[0], self.locators.table_value[1].format(row))
        actual_value = self.find_element(locator).text
        assert_that(actual_value, f"Modal Window Table Row: {row}").is_equal_to(str(expected_value))
    # endregion
