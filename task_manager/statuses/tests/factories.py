import factory
from task_manager.statuses.models import Status
from task_manager.users.tests.factories import UserFactory


class StatusFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Status

    name = factory.Faker('word')
    user = UserFactory()
