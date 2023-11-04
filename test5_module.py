from typing import Any
from datetime import date as dt


global_x = 100


def setup():
    global global_x
    global_x = global_x + 10
    return global_x


class Counter:
    def __init(self):
        self.x = 0

    def setup(self, x) -> any:
        self.x = x
        return self


class App:
    def __init__(self):
        global global_x
        global_x = global_x + 10
        self.x = global_x

    def setup(self):
        global global_x
        global_x = global_x + 10
        return Counter().setup(self.x)


class StudentData:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


class StudentData:
    def __init__(self, name: str, birthday: list):
        self.name: str = name
        self.birthday: dt = dt(*birthday)

    def __str__(self):
        return f"name {self.name}: birthday {self.birthday}"


class Student:
    def __init__(self, name: str, birthday: dt):
        self.s_data = StudentData(name, birthday)
        self.grade = 0

    def data(self):
        return self.s_data
