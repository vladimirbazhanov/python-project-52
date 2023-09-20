import factory
from task_manager.tasks.models import Task
from task_manager.users.tests.factories import UserFactory
from task_manager.statuses.tests.factories import StatusFactory


class TaskFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Task

    name = factory.Faker('word')
    description = factory.Faker('sentence')
    status = factory.SubFactory(StatusFactory)
    user = factory.SubFactory(UserFactory)
    executor = factory.SubFactory(UserFactory)

