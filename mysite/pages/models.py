import datetime

from django.db import models
from django.utils import timezone
import datetime

class User(models.Model):		
    name_text = models.CharField(max_length = 200)
    def __str__(self):
        return self.name_text


# Create your models here.
class ToDoList(models.Model):
	name = models.CharField(default="Untitled Todolist", max_length=200)

	def __str__(self):
		return self.name

class Task(models.Model):
    complete = models.BooleanField(default=False)
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    description_text = models.CharField(default="Untitled Task", max_length=200)
    due_date = models.DateTimeField('Due Date', default=timezone.now())
    time_estimate = models.IntegerField(default=0)
    task_id = models.CharField(default="default_id", max_length=200)
    def __str__(self):
        return self.description_text 

class WebsiteMeta(models.Model):		
    total_tasks_created = models.IntegerField(default = 0)

