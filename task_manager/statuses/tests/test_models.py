from django.test import TestCase
from faker import Faker
import factory
from task_manager.statuses.models import Status
from task_manager.users.tests.factories import UserFactory
fake = Faker()


class StatusFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Status
    name = 'status'


class StatusCreateTestCase(TestCase):
    def test_create_status_model(self):
        name = fake.word()
        user = UserFactory()

        status = StatusFactory(name=name, user=user)
        self.assertEquals(status.name, name)
        self.assertEquals(status.__str__(), name)
