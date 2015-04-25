from django.conf.urls import patterns, include, url
from task.views import Home, TaskView, TaskDetail, CreateUser

urlpatterns = patterns(
    '',
    url(r'^$', Home.as_view(), name='home'),
    url(r'^task/$', TaskView.as_view(), name='task'),
    url(r'^task/(?P<pk>\d+)/$', TaskDetail.as_view(), name='task_detail'),
    url(r'^create_user/$', CreateUser.as_view(), name='create_user'),
)
