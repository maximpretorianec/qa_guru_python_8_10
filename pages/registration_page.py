from selene import have, be, browser
from utils.load_file import path
from models.user import test_user_data


class Registration:

    def register_user(self):
        browser.element("#firstName").type(test_user_data.first_name)
        browser.element("#lastName").type(test_user_data.last_name)
        browser.element("#userEmail").type(test_user_data.email)
        browser.element("#userNumber").type(test_user_data.mobile)
        browser.element("#currentAddress").type(test_user_data.address)
        browser.element("#subjectsInput").type(test_user_data.subject).press_enter()
        browser.all('input[name=gender]').element_by(have.value(test_user_data.gender)).element('..').click()
        browser.all('.custom-checkbox').element_by(have.exact_text(test_user_data.hobby)).click()
        browser.element('#dateOfBirthInput').should(be.not_.blank).click()
        browser.element('.react-datepicker__month-select').type(test_user_data.date_of_birth.strftime('%B'))
        browser.element('.react-datepicker__year-select').type(test_user_data.date_of_birth.year)
        browser.element(
            f'.react-datepicker__day--0{test_user_data.date_of_birth.day}:not(.react-datepicker__day--outside-month)').click()
        browser.element("#uploadPicture").send_keys(path(test_user_data.picture))
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(test_user_data.state)).click()
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(test_user_data.city)).click()
        browser.element('#submit').press_enter()

    def assert_registration_data(self):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                f'{test_user_data.first_name} {test_user_data.last_name}',
                test_user_data.email,
                test_user_data.gender,
                test_user_data.mobile,
                test_user_data.date_of_birth.strftime('%d %B,%Y'),
                test_user_data.subject,
                test_user_data.hobby,
                test_user_data.picture,
                test_user_data.address,
                f'{test_user_data.state} {test_user_data.city}',
            )
        )
