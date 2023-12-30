from pages.registration_page import Registration
from models.user import test_user_data


def test_user_registration_form():
    registration_page = Registration()

    registration_page.open()
    registration_page.register_user(test_user_data)
    registration_page.assert_registration_data(test_user_data)
