import faker


def get_data_from_requirements() -> list:
    with open('requirements.txt') as file:
        return file.readlines()


def get_fake_users(qty) -> list:
    fake = faker.Faker()
    users = []
    for _ in range(qty):
        users.append(f"{fake.email()} {fake.name()}")
    return users
