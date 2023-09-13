from django.test import TestCase
from faker import Faker
import factory
from task_manager.labels.models import Label
from task_manager.users.tests.factories import UserFactory
fake = Faker()


class LabelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Label
    name = 'label'


class LabelCreateTestCase(TestCase):
    def test_create_label_model(self):
        name = fake.word()
        user = UserFactory()

        label = LabelFactory(name=name, user=user)
        self.assertEquals(label.name, name)
        self.assertEquals(label.__str__(), name)
