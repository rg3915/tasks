from django.views.generic import ArchiveIndexView
from django.views.generic import DetailView

from task.models import Task


class TaskView(ArchiveIndexView):
    model = Task
    date_field = 'created_at'


class TaskDetail(DetailView):
    model = Task

__all__ = [
    'TaskView',
]
