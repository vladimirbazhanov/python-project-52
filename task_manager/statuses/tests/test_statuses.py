from django.test import TestCase, Client
from django.urls import reverse
from task_manager.statuses.models import Status
from task_manager.users.models import User


class StatusesTestCase(TestCase):
    fixtures = ['users', 'statuses']

    def setUp(self):
        self.client = Client()
        self.status1 = Status.objects.first()
        self.status2 = Status.objects.last()
        self.user1 = User.objects.first()
        self.client.force_login(self.user1)

    def test_list_statuses(self):
        url = reverse('statuses:index')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.status1.name)
        self.assertNotContains(response, self.status2.name)

    def test_create_status(self):
        response = self.client.post(reverse('statuses:create'), {'name': 'status_3'}, follow=True)
        self.assertContains(response, 'Статус успешно создан')
        self.assertContains(response, 'status_3')
        self.assertEquals(Status.objects.count(), 3)

    def test_update_status(self):
        url = reverse('statuses:update', kwargs={'id': self.status1.id})
        response = self.client.post(url, {'name': 'new_status'}, follow=True)
        self.assertContains(response, 'Статус успешно изменен')
        self.assertContains(response, 'new_status')

    def test_delete_status(self):
        url = reverse('statuses:delete', kwargs={'id': self.status1.id})
        response = self.client.post(url, follow=True)
        self.assertContains(response, 'Статус успешно удален')
