from django.test import TestCase, Client
from faker import Faker
from task_manager.tasks.models import Task
from task_manager.users.tests.factories import UserFactory
from task_manager.labels.tests.factories import LabelFactory
from task_manager.statuses.tests.factories import StatusFactory
from django.urls import reverse


class CreateTaskTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.fake = Faker()
        self.create_and_login_test_user(self)

    def test_create_task(self):
        label = LabelFactory(user=self.user)
        status = StatusFactory(user=self.user)

        request = {
            'name': self.fake.word(),
            'description': self.fake.sentence(),
            'labels': [label.id],
            'status': status.id,
            'executor': self.user.id
        }
        response = self.client.post(reverse('tasks:create'), request, follow=True)
        self.assertRedirects(response, reverse('tasks:index'))
        self.assertContains(response, 'Задача успешно создана')
        self.assertEqual(Task.objects.count(), 1)

    @staticmethod
    def create_and_login_test_user(self):
        self.user = UserFactory()
        self.user.set_password('12345678_qwerty')
        self.user.save()
        self.client.login(username=self.user.username, password='12345678_qwerty')
