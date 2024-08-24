from enum import Enum


class Gender(Enum):
    MALE = 1
    FEMALE = 2
    OTHER = 3

    def __str__(self):
        return str(self.name).capitalize()

    def __repr__(self):
        return str(self.name).capitalize()


class Hobby(Enum):
    SPORTS = 1
    READING = 2
    MUSIC = 3

    def __str__(self):
        return str(self.name).capitalize()

    def __repr__(self):
        return str(self.name).capitalize()
