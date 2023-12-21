import dataclasses
import datetime


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile: str
    date_of_birth: datetime.date
    subject: str
    hobby: str
    picture: str
    address: str
    state: str
    city: str


test_user_data = User(first_name='RandomName',
                      last_name='RandomFamilyName',
                      email='user@qa.com',
                      gender='Male',
                      mobile='9991111111',
                      date_of_birth=datetime.date(year=1993, month=9, day=24),
                      subject='Arts',
                      hobby='Music',
                      picture='Duck.jpg',
                      address='Street',
                      state='Uttar Pradesh',
                      city='Lucknow')
