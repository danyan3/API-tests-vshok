from packages import fake
import random


def random_register_payload():
    email = fake.email()
    password = fake.password(length=random.randint(5, 20))
    age = random.randint(0, 99)

    return {
        'email': email,
        'password': password,
        'age': age
    }
