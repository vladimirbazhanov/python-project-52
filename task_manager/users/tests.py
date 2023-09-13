import factory
from task_manager.users.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
