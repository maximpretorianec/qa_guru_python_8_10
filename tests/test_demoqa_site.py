from pages.registration_page import Registration


def test_user_registration_form():
    registration_page = Registration()

    registration_page.open()
    registration_page.register_user()
    registration_page.assert_registration_data()
