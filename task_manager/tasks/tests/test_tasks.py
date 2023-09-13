from django.test import TestCase, Client
from faker import Faker
from task_manager.users.tests.factories import UserFactory


class CreateTaskTestCase(TestCase):
    client = Client()
    fake = Faker()

    def setUp(self) -> None:
        user = UserFactory()

    def test_create_task(self):
        request = {
            'name': self.fake.word()
        }
        response = self.client.post('/tasks/create', request)
        print(response)
        self.assertEqual(response.status_code, 200)