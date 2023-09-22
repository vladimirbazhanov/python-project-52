from django.test import TestCase, Client
from django.urls import reverse
from task_manager.users.tests.factories import UserFactory


class UsersViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = UserFactory()
        self.user2 = UserFactory()

    def test_users_view(self):
        url = reverse('users:index')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user1.first_name)
        self.assertContains(response, self.user2.first_name)
