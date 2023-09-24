import factory
from task_manager.labels.models import Label
from task_manager.users.tests.factories import UserFactory


class LabelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Label

    name = factory.Faker('word')
    user = factory.SubFactory(UserFactory)
