import datetime

from django.db import models
from django.utils import timezone

class User(models.Model):		
    name_text = models.CharField(max_length = 200)
    def __str__(self):
        return self.name_text


# Create your models here.
class ToDoList(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Task(models.Model):
	complete = models.BooleanField()
	todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    description_text = models.CharField(max_length=200)
    due_date = models.DateTimeField('Due Date')
    time_estimate = models.IntegerField(default=0)
    def __str__(self):
        return self.description_text 

