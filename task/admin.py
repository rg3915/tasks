from django.contrib.admin import site
from django.contrib.admin import ModelAdmin

from task.models import Task, Customer, Seller


class TaskAdmin(ModelAdmin):
    list_display = ['name', 'description', 'created_at', 'finalized']
    # exclude = ['created_at']
    fields = ['name', 'description', 'finalized']
    list_editable = ['finalized']
    search_fields = ['name']


class SellerAdmin(ModelAdmin):
    list_display = ['full_name', 'email', 'internal', 'active']

site.register(Task, TaskAdmin)
site.register(Customer)
site.register(Seller, SellerAdmin)
