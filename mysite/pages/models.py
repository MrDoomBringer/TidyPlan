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

class Course(models.Model):
    name = models.CharField(default = "untitled course", max_length=25)
    color = models.CharField(default = "#F6F6F6", max_length=7)
    def __str__(self):
        return self.name

class Task(models.Model):
    complete = models.BooleanField(default=False)
    todo_list = models.ForeignKey(ToDoList, null=True, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name="courses", null=True, on_delete=models.CASCADE)
    description_text = models.CharField(default="Untitled Task", max_length=200)
    due_date = models.DateTimeField('Due Date', default=timezone.now)
    time_estimate = models.IntegerField(default=0)
    initial_subtask_count = models.IntegerField(default=0)
    is_subtask = models.BooleanField(default=False)
    parent_task = models.ForeignKey('self', related_name="subtasks", null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.description_text

class WebsiteMeta(models.Model):		
    total_tasks_created = models.IntegerField(default = 0)
    total_courses_created = models.IntegerField(default = 0)

