from django.contrib.admin import site
from django.contrib.admin import ModelAdmin

from task.models import Task


class TaskAdmin(ModelAdmin):
    list_display = ['name', 'description', 'created_at', 'finalized']
    # exclude = ['created_at']
    fields = ['name', 'description', 'finalized']
    list_editable = ['finalized']
    search_fields = ['name']

site.register(Task, TaskAdmin)
