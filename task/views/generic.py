from django.views.generic import ArchiveIndexView

from task.models import Task


class TaskView(ArchiveIndexView):
    model = Task

__all__ = [
    'TaskView',
]
