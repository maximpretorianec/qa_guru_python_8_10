from selene import have, be, browser
from utils.load_file import path
from models.user import User


class Registration:

    def open(self):
        browser.open('/automation-practice-form')

    def register_user(self, user_data: User):
        browser.element("#firstName").type(user_data.first_name)
        browser.element("#lastName").type(user_data.last_name)
        browser.element("#userEmail").type(user_data.email)
        browser.element("#userNumber").type(user_data.mobile)
        browser.element("#currentAddress").type(user_data.address)
        browser.element("#subjectsInput").type(user_data.subject).press_enter()
        browser.all('input[name=gender]').element_by(have.value(user_data.gender)).element('..').click()
        browser.all('.custom-checkbox').element_by(have.exact_text(user_data.hobby)).click()
        browser.element('#dateOfBirthInput').should(be.not_.blank).click()
        browser.element('.react-datepicker__month-select').type(user_data.date_of_birth.strftime('%B'))
        browser.element('.react-datepicker__year-select').type(user_data.date_of_birth.year)
        browser.element(
            f'.react-datepicker__day--0{user_data.date_of_birth.day}:not(.react-datepicker__day--outside-month)').click()
        browser.element("#uploadPicture").send_keys(path(user_data.picture))
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(user_data.state)).click()
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(user_data.city)).click()
        browser.element('#submit').press_enter()

    def assert_registration_data(self, user_data: User):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                f'{user_data.first_name} {user_data.last_name}',
                user_data.email,
                user_data.gender,
                user_data.mobile,
                user_data.date_of_birth.strftime('%d %B,%Y'),
                user_data.subject,
                user_data.hobby,
                user_data.picture,
                user_data.address,
                f'{user_data.state} {user_data.city}',
            )
        )
