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

    def test_create_label(self):
        response = self.client.post(reverse('labels:create'), {'name': 'label_3'}, follow=True)
        self.assertContains(response, 'Метка успешно создана')
        self.assertContains(response, 'label_3')
        self.assertEquals(Label.objects.count(), 3)

    def test_update_label(self):
        url = reverse('labels:update', kwargs={'id': self.label1.id})
        response = self.client.post(url, {'name': 'new_label'}, follow=True)
        self.assertContains(response, 'Метка успешно изменена')
        self.assertContains(response, 'new_label')

    def test_delete_label(self):
        url = reverse('labels:delete', kwargs={'id': self.label1.id})
        response = self.client.post(url, follow=True)
        self.assertContains(response, 'Метка успешно удалена')
