from pages.registration_page import Registration


def test_user_registration_form():
    registration_page = Registration()
    registration_page.open()
    registration_page.set_first_name('RandomName')
    registration_page.set_last_name('RandomFamilyName')
    registration_page.set_email('user@qa.com')
    registration_page.set_mobile('9991111111')
    registration_page.set_current_address('Street')
    registration_page.set_subject('Arts')
    registration_page.set_gender()
    registration_page.set_hobbies()
    registration_page.select_state('Uttar Pradesh')
    registration_page.select_city('Lucknow')
    registration_page.set_birthday(day=24, month='September', year=1993)
    registration_page.upload_picture('Duck.jpg')
    registration_page.submit()

    registration_page.assert_registration_data(
        first_name='RandomName', last_name='RandomFamilyName', email='user@qa.com', mobile='9991111111',
        address='Street', subject='Arts', gender='Male', hobbie='Music', state='Uttar Pradesh', city='Lucknow',
        day=24, month='September', year=1993, picture='Duck.jpg'
    )
