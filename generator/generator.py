import random
import datetime

from data.data import Person
from faker import Faker


faker_ru = Faker('ru_RU')
faker_en = Faker('en')
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        age=random.randint(16, 80),
        salary=random.randint(20000, 180000),
        department=faker_ru.job(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
        mobile=faker_ru.msisdn(),
    )


def generated_file():
    path = f'/Users/timur/PycharmProjects/demoqa_autotests/test_file_{datetime.date.today()}' \
           f'.{random.choice(["txt", "pdf"])}'
    file = open(path, 'w+')
    file.write('HELLO AQA WORLD!')
    file.close()
    return file.name, path
