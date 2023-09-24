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
