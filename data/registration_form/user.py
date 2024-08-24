import datetime
from dataclasses import dataclass
from typing import List, Text

from data.registration_form.enums import Gender, Hobby


@dataclass
class User:
    first_name: Text
    last_name: Text
    email: Text
    gender: Gender
    phone_number: Text
    date_of_birth: datetime.date
    subjects: List[Text]
    hobbies: List[Hobby]
    picture: Text
    address: Text
    state: Text
    city: Text
