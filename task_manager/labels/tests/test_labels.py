from django.test import TestCase, Client
from django.urls import reverse
from task_manager.labels.models import Label
from task_manager.users.models import User


class LabelsTestCase(TestCase):
    fixtures = ['users', 'labels']

    def setUp(self):
        self.client = Client()
        self.label1 = Label.objects.first()
        self.label2 = Label.objects.last()
        self.user1 = User.objects.first()
        self.client.force_login(self.user1)

    def test_list_labels(self):
        url = reverse('labels:index')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.label1.name)
        self.assertNotContains(response, self.label2.name)
