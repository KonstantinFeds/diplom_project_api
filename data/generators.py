from faker import Faker

fake = Faker()


def payload_generate_user():
    return {
        "id": fake.random_int(min=1, max=1000),
        "username": fake.user_name()[:20],
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "email": fake.email(),
        "password": fake.password(length=10),
        "phone": fake.phone_number()[:15],
        "userStatus": fake.random_int(min=0, max=1),
    }
