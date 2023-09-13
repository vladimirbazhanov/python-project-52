from django.test import TestCase
from faker import Faker
import factory
from task_manager.labels.models import Label
from task_manager.users.tests import UserFactory
fake = Faker()


class LabelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Label
    name = 'label'


class LabelTestCase(TestCase):
    def test_create_label(self):
        name = fake.word()
        user = UserFactory()

        label = LabelFactory(name=name, user=user)
        self.assertEquals(label.name, name)
        self.assertEquals(label.__str__(), name)
