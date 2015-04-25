from django.conf.urls import patterns, include, url
from task.views import Home, TaskView, TaskDetail

urlpatterns = patterns(
    '',
    url(r'^$', Home.as_view(), name='home'),
    url(r'^task/$', TaskView.as_view(), name='task'),
    url(r'^task/(?P<pk>\d+)/$', TaskDetail.as_view(), name='task_detail'),
)
