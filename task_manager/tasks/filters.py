import django_filters

from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task
from task_manager.users.models import User


class TaskFilter(django_filters.FilterSet):
    class Meta:
        model = Task
        fields = ['status', 'executor', 'label', 'only_my']

    status = django_filters.ModelChoiceFilter(field_name='status', queryset=Status.objects.all())
    executor = django_filters.ModelChoiceFilter(field_name='executor', queryset=User.objects.all())
    label = django_filters.ModelMultipleChoiceFilter(
        field_name='labels',
        queryset=Label.objects.all()
    )
    only_my = django_filters.CharFilter(field_name='only_my', method='filter_only_my')

    def filter_only_my(self, queryset, name, value):
        if value == 'on':
            return queryset.filter(user_id=self.request.user.id)
        else:
            return queryset
