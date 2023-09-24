from django.test import TestCase
from task_manager.statuses.tests.factories import StatusFactory


class StatusCreateTestCase(TestCase):
    def test_create_status_model(self):
        status = StatusFactory(name='New')
        self.assertEquals(status.name, 'New')
        self.assertEquals(status.__str__(), 'New')
