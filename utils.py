from csv import DictReader

import faker

INCHES_TO_CM = 2.54
POUNDS_TO_KG = 0.45359237

def get_data_from_requirements() -> list:
    with open('requirements.txt') as file:
        return file.readlines()


def get_fake_users(qty) -> list:
    fake = faker.Faker()
    users = []
    for _ in range(qty):
        users.append(f"{fake.email()} {fake.name()}")
    return users


def inches_to_cm(value):
    return value * INCHES_TO_CM


def pounds_to_kg(value):
    return value * INCHES_TO_CM


def get_avg_data_from_csv(file_name):
    total_rows = 0
    height = 0
    weight = 0
    with open(file_name, newline='') as csv_file:
        reader = DictReader(csv_file)
        for row in reader:
            height += float(row[' "Height(Inches)"'])
            weight += float(row[' "Weight(Pounds)"'])
            total_rows += 1
    return (
        inches_to_cm(height / total_rows) if total_rows else 0,
        pounds_to_kg(weight / total_rows) if total_rows else 0
    )
