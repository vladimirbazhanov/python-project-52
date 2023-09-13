import factory
from task_manager.tasks.models import Task
from task_manager.users.tests.factories import UserFactory
from task_manager.statuses.tests.factories import StatusFactory


class TaskFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Task

    name = factory.Faker('word')
    description = factory.Faker('sentence')
    status = StatusFactory()
    user = UserFactory()
    executor = UserFactory()

    @factory.post_generation
    def labels(self, create, extracted, **kwargs):
        if not create or not extracted:
            return
        self.labels.add(*extracted)