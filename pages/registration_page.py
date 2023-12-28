from selene import have, be, browser
from utils.load_file import path

import random


class Registration:

    def open(self):
        browser.open('/automation-practice-form')

    def set_first_name(self, first_name):
        browser.element("#firstName").type(first_name)

    def set_last_name(self, last_name):
        browser.element("#lastName").type(last_name)

    def set_email(self, email):
        browser.element("#userEmail").type(email)

    def set_mobile(self, mobile):
        browser.element("#userNumber").type(mobile)

    def set_current_address(self, address):
        browser.element("#currentAddress").type(address)

    def set_subject(self, subject):
        browser.element("#subjectsInput").type(subject).press_enter()

    def set_gender(self):
        browser.element('[for="gender-radio-1"]').click()

    def set_hobbies(self):
        browser.element('[for="hobbies-checkbox-3"]').click()

    def select_state(self, state):
        browser.element("#state").click().all('[id^="react-select-3-option"]').element_by(have.exact_text(state)).click()

    def select_city(self, city):
        browser.element("#city").click().all('[id^="react-select-4-option"]').element_by(have.exact_text(city)).click()

    def set_birthday(self, day, month, year):
        browser.element('#dateOfBirthInput').should(be.not_.blank).click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()

    def upload_picture(self, picture):
        browser.element("#uploadPicture").send_keys(path(picture))

    def submit(self):
        browser.element("#userNumber").press_enter()

    def assert_registration_data(self, first_name, last_name, email, mobile, address, subject, gender, hobbie, state,
                                 city, day, month, year, picture):
        browser.element('.table-responsive').all('td:nth-child(2)').should(
            have.texts(f"{first_name} {last_name}", email, gender, mobile, f"{day} {month},{year}",
                       subject, hobbie, picture, address, f"{state} {city}"))
