from django.test import TestCase, Client
from django.urls import reverse
from task_manager.users.models import User


class UsersTestCase(TestCase):
    fixtures = ['users']

    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.first()
        self.user2 = User.objects.last()

    def test_list_users(self):
        url = reverse('users:index')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user1.first_name)
        self.assertContains(response, self.user2.first_name)

    def test_login_user(self):
        response = self.client.get(reverse('login'))
        self.assertContains(response, 'Вход')

        user_data = {'username': self.user1.username, 'password': 'password_qwerty'}
        response = self.client.post(reverse('login'), user_data, follow=True)

        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'Вы залогинены')
        self.assertContains(response, 'Выход')

    def test_logout_user(self):
        self.client.force_login(self.user2)

        response = self.client.get(reverse('index'))
        self.assertContains(response, 'Выход')

        response = self.client.post(reverse('logout'), follow=True)
        self.assertContains(response, 'Вы разлогинены')
        self.assertContains(response, 'Вход')

    def test_create_user(self):
        response = self.client.get(reverse('users:create'))
        self.assertContains(response, 'Регистрация')

        response = self.client.post(reverse('users:create'), self.user_data(), follow=True)
        self.assertContains(response, 'Пользователь успешно зарегистрирован')
        self.assertEquals(User.objects.count(), 3)  # two from fixtures and one created here

    def test_update_user(self):
        self.client.force_login(self.user1)

        response = self.client.get(
            reverse('users:update', kwargs={'id': self.user2.id}), follow=True
        )
        self.assertContains(response, 'У вас нет прав для изменения другого пользователя.')

        response = self.client.get(reverse('users:update', kwargs={'id': self.user1.id}))

        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'Изменение пользователя')

        response = self.client.post(
            reverse('users:update', kwargs={'id': self.user1.id}), self.user_data(), follow=True
        )
        self.assertContains(response, 'Пользователь успешно изменен')

    def test_delete_user(self):
        self.client.force_login(self.user1)

        response = self.client.get(
            reverse('users:delete', kwargs={'id': self.user2.id}), follow=True
        )
        self.assertContains(response, 'У вас нет прав для изменения другого пользователя.')

        response = self.client.get(reverse('users:delete', kwargs={'id': self.user1.id}))

        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'Удаление пользователя')

        response = self.client.post(
            reverse('users:delete', kwargs={'id': self.user1.id}), follow=True
        )
        self.assertContains(response, 'Пользователь успешно удален')

    def user_data(self):
        return {
            'username': 'test',
            'first_name': 'Test',
            'last_name': 'User',
            'password1': 'password_qwerty',
            'password2': 'password_qwerty'
        }
