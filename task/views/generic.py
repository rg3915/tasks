from django.views.generic import ArchiveIndexView
from django.views.generic import DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from task.models import Task


class TaskView(ArchiveIndexView):
    model = Task
    date_field = 'created_at'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        self.queryset = Task.objects.filter(user=request.user.id)
        return super().get(request, *args, **kwargs)


class TaskDetail(DetailView):
    model = Task

__all__ = [
    'TaskView',
    'TaskDetail',
]
