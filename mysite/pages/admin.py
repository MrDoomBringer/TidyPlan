from django.contrib import admin

from .models import ToDoList, User, Task, WebsiteMeta

admin.site.register(User)
admin.site.register(Task)
admin.site.register(ToDoList)
admin.site.register(WebsiteMeta)