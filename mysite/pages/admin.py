from django.contrib import admin

from .models import Task, WebsiteMeta

admin.site.register(Task)
admin.site.register(WebsiteMeta)