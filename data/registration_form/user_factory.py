import os
import random

from faker import Faker

from data.registration_form.enums import Gender, Hobby
from data.registration_form.user import User

faker = Faker()

subjects = ["Physics", "English", "Chemistry", "Computer Science"]
state_and_cities = {
    "NCR": ["Delhi", "Gurgaon", "Noida"],
    "Uttar Pradesh": ["Agra", "Lucknow", "Merrut"],
    "Haryana": ["Karnal", "Panipat"],
    "Rajasthan": ["Jaipur", "Jaiselmer"]
}


class UserFactory:
    """
    Provides Static Factory Methods for User generation.
    """

    @staticmethod
    def create_random_user() -> User:
        return User(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            email=faker.email(),
            gender=random.choice(list(Gender)),
            phone_number=str(faker.random_number(digits=10, fix_len=True)),
            date_of_birth=faker.date_of_birth(),
            # Provides non-empty list of subjects and hobbies
            subjects=random.sample(subjects, k=random.randint(1, len(subjects))),
            hobbies=random.sample(list(Hobby), k=random.randint(1, len(Hobby))),
            picture=os.path.join(os.getcwd(), "resources/images/image.jpg"),
            address=faker.address().replace("\n", ""),
            state=(random_state := random.choice(list(state_and_cities.keys()))),
            city=random.choice(state_and_cities[random_state])
        )
