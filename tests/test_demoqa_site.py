from pages.registration_page import Registration


def test_user_registration_form():
    test_data = {'first_name': 'RandomName', 'last_name': 'RandomFamilyName', 'email': 'user@qa.com',
                 'mobile': '9991111111', 'address': 'Street', 'subject': 'Arts',
                 'birth_day': 24, 'birth_month': 'September', 'birth_year': 1993, 'picture': 'Duck.jpg',
                 'state': 'Uttar Pradesh', 'city': 'Lucknow'}
    registration_page = Registration()
    registration_page.set_first_name(test_data['first_name'])
    registration_page.set_last_name(test_data['last_name'])
    registration_page.set_email(test_data['email'])
    registration_page.set_mobile(test_data['mobile'])
    registration_page.set_current_address(test_data['address'])
    registration_page.set_subject(test_data['subject'])
    test_data['gender'] = registration_page.select_gender()
    test_data['hobbie'] = registration_page.select_hobbies()

    registration_page.select_state(test_data['state'])
    registration_page.select_city(test_data['city'])
    registration_page.set_birthday(day=test_data['birth_day'], month=test_data['birth_month'],
                                   year=test_data['birth_year'])
    registration_page.upload_picture(test_data['picture'])
    registration_page.submit()

    registration_page.assert_registration_data(
        first_name=test_data['first_name'], last_name=test_data['last_name'], email=test_data['email'],
        mobile=test_data['mobile'], address=test_data['address'], subject=test_data['subject'],
        gender=test_data['gender'], hobbie=test_data['hobbie'], state=test_data['state'], city=test_data['city'],
        day=test_data['birth_day'], month=test_data['birth_month'], year=test_data['birth_year'],
        picture=test_data['picture']
    )
