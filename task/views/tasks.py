from django.views.generic import View

from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template.context import RequestContext

from task.models import Task
from task.forms import UserCreateForm


class Home(View):
    template_name = 'task/home.html'
    context = {}

    def get(self, request, *args, **kwargs):
        self.context['counter'] = Task.objects.filter(finalized=False).count()
        return render_to_response(self.template_name, self.context, RequestContext(request))


class CreateUser(View):
    template_name = 'task/create_user.html'
    context = {}

    def get(self, request, *args, **kwargs):
        self.context['form'] = UserCreateForm()
        return render_to_response(self.template_name, self.context, RequestContext(request))

    def post(self, request, *args, **kwargs):
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            self.context['form'] = form
        return render_to_response(self.template_name, self.context, RequestContext(request))

__all__ = [
    'Home',
    'CreateUser',
]
