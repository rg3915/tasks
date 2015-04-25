from django.conf.urls import patterns, include, url
from django.contrib import admin
import task.urls

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(task.urls))
)
