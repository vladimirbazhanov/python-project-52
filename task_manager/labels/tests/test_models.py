from django.test import TestCase
from task_manager.labels.tests.factories import LabelFactory


class LabelCreateTestCase(TestCase):
    def test_create_label_model(self):
        label = LabelFactory.create(name='TestLabel')

        self.assertEquals(label.name, 'TestLabel')
        self.assertEquals(label.__str__(), 'TestLabel')
