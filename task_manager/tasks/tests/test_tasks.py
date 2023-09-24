from django.test import TestCase, Client
from faker import Faker

from task_manager.labels.models import Label
from task_manager.tasks.models import Task
from task_manager.users.models import User
from task_manager.statuses.models import Status
from django.urls import reverse


class CreateTaskTestCase(TestCase):
    fixtures = ['users', 'labels', 'statuses', 'tasks']

    def setUp(self):
        self.client = Client()
        self.fake = Faker()
        self.user = User.objects.first()
        self.label = Label.objects.first()
        self.status = Status.objects.first()
        self.task1 = Task.objects.first()
        self.task2 = Task.objects.last()
        self.client.force_login(self.user)

    def test_list_tasks(self):
        response = self.client.get(reverse('tasks:index'))
        self.assertContains(response, self.task1.name)
        self.assertContains(response, self.task2.name)

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
        self.assertEqual(Task.objects.count(), 3)  # two from fixtures and one created here

    def test_update_task(self):
        task_data = {
            'name': 'New name',
            'description': 'New description',
            'labels': [self.label.id],
            'status': self.status.id,
            'executor': self.user.id
        }
        url = reverse('tasks:update', kwargs={'id': self.task1.id})
        response = self.client.post(url, task_data, follow=True)
        self.assertContains(response, 'Задача успешно изменена')
        self.assertContains(response, 'New name')

    def test_delete_task(self):
        url = reverse('tasks:delete', kwargs={'id': self.task1.id})
        response = self.client.post(url, follow=True)
        self.assertContains(response, 'Задача успешно удалена')
        self.assertEquals(Task.objects.count(), 1)
