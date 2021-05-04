from django import forms
from .models import Course, Task
from django.utils import timezone

class CourseForm(forms.ModelForm):
	class Meta:
		model = Course
		fields = ('name',)
class TaskForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = ('description_text','due_date')

class CreateNewList(forms.Form):
	name = forms.CharField(label = "Name", max_length = 200)
	check = forms.BooleanField()

