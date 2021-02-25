from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Task
def index(response, name_text):
	tsk_list = User.objects.get(name_text = name_text)
	return render(response, "homepage/tasks.html",{})

def home(response):
	return render(response, "homepage/home.html",{})