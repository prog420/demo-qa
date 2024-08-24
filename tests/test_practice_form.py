import allure
import pytest
from assertpy import soft_assertions

from app.ui.pages.practice_form_page import PracticeFormPage
from data.registration_form.user_factory import UserFactory
from tests.base_case import BaseCase


@allure.feature("Practice Form")
class TestPracticeForm(BaseCase):
    @allure.id("TC-001")
    @allure.title("Submitting form with valid data")
    @allure.description("This test generates random user, fill form with its data and check if saved data is correct.")
    def test_practice_form_submitting(self):
        # Arrange
        random_user = UserFactory.create_random_user()
        page = PracticeFormPage(self.driver)
        expected_title = "Thanks for submitting the form"
        # Act
        page.open()
        page.fill_form(random_user)
        page.submit_form()
        # Assert
        with soft_assertions():
            page.assert_modal_title_equal_to(expected_title)
            page.assert_saved_data_matches_user(random_user)

    @pytest.mark.xfail(reason="Failed test to demonstrate attachments")
    @allure.id("TC-002")
    @allure.title("[xfail] Submitting form with valid data")
    def test_practice_form_submitting_failed(self):
        # Arrange
        random_user = UserFactory.create_random_user()
        page = PracticeFormPage(self.driver)
        expected_title = "Title"
        # Act
        page.open()
        page.fill_form(random_user)
        page.submit_form()
        # Assert
        with soft_assertions():
            page.assert_modal_title_equal_to(expected_title)
            page.assert_saved_data_matches_user(random_user)
