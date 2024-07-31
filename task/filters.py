import django_filters
from .models import Task

class TaskFilter(django_filters.FilterSet):
    class Meta:
        model = Task
        fields = {
            'priority': ['exact'],
            'current_status': ['exact'],
            'due_date': ['exact', 'lt', 'gt'],
            'created_at': ['exact', 'lt', 'gt']
        }