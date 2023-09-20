from django.test import TestCase
from task_manager.tasks.tests.factories import TaskFactory
from task_manager.users.tests.factories import UserFactory


class TaskCreateTestCase(TestCase):
    def test_create_task_model(self):
        task = TaskFactory(
            name='Test task',
            description='with description'
        )

        self.assertEquals(task.name, 'Test task')
        self.assertEquals(task.__str__(), 'Test task with description')
