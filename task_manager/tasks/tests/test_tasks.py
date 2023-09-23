from django.test import TestCase, Client
from faker import Faker

from task_manager.labels.models import Label
from task_manager.tasks.models import Task
from task_manager.users.models import User
from task_manager.statuses.models import Status
from django.urls import reverse


class CreateTaskTestCase(TestCase):
    fixtures = ['users', 'labels', 'statuses']

    def setUp(self):
        self.client = Client()
        self.fake = Faker()
        self.user = User.objects.first()
        self.label = Label.objects.first()
        self.status = Status.objects.first()
        self.client.force_login(self.user)

    def test_create_task(self):
        task_data = {
            'name': self.fake.word(),
            'description': self.fake.sentence(),
            'labels': [self.label.id],
            'status': self.status.id,
            'executor': self.user.id
        }
        response = self.client.post(reverse('tasks:create'), task_data, follow=True)
        self.assertRedirects(response, reverse('tasks:index'))
        self.assertContains(response, 'Задача успешно создана')
        self.assertEqual(Task.objects.count(), 1)
