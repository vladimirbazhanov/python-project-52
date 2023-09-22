import pytest
import factory


@pytest.fixture
def user_params():
    return {
        'first_name': factory.Faker('first_name'),
        'last_name': factory.Faker('last_name'),
        'username': factory.Sequence(lambda n: 'user_{}'.format(n)),
        'password1': 'password_qwerty',
        'password2': 'password_qwerty'
    }
