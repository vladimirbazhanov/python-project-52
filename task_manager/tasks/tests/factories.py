import factory
from task_manager.tasks.models import Task
from task_manager.users.tests.factories import UserFactory
from task_manager.statuses.tests.factories import StatusFactory
from task_manager.labels.tests.factories import LabelFactory


class TaskFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Task

    name = factory.Faker('word')
    description = factory.Faker('sentence')
    labels = [LabelFactory()]
    status = StatusFactory()
    user = UserFactory()
    executor = UserFactory()
