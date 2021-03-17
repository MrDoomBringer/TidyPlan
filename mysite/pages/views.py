from django.http import HttpResponse
from .models import ToDoList
from .forms import CreateNewList
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import User, Task, WebsiteMeta


def index(request):
	template_name = 'pages/home.html'
	return render(request, template_name)

def faq(request):
	return HttpResponse("FAQ")

def howto(request):
	return HttpResponse("How To")

def account(request):
	return HttpResponse("Account Page")

#See tasks.html for related HTML code
def calendar(request):
	if (request.method == "POST"):
		if ('new_task' in request.POST): #If the form that we submitted has the name 'new_task'
			check_websitemeta()
			td = ToDoList()
			td.save()
			t = Task()
			t.description_text = f'Task number [{total_tasks_ever_made()}]'
			t.todolist = td
			t.task_id=timezone.now()
			t.save()
			total_tasks_ever_made(increment=1)

		if ('delete_task' in request.POST): #If the form that we submitted has the name 'delete_task'
			id_to_delete = request.POST['deleted_task'] #Get the ID of the task. This is stored in a input tag of type='hidden'
			Task.objects.filter(task_id=id_to_delete).delete()
	
	tsk_list = Task.objects.filter(due_date__lte=timezone.now()).order_by('-due_date')
	return render(request, 'pages/tasks.html', {'tsk_list': tsk_list})

def tos(request):
	return HttpResponse("Terms of Service")

def create(response):
	if response.method == "POST":
		form = CreateNewList(response.POST)
		if form.is_valid():
			n = form.cleaned_data["name"]
			t = ToDoList(name=n)
			t.save()

		return HttpResponseRedirect("/%i" %t.id)
	else:
		form = CreateNewList()
	return render(response, "pages/create.html", {"form": form})

#Check to see if we have a 'WebsiteMeta' object in the database. If not, add one
def check_websitemeta():
	#Use objects.all() to get a list of all 'WebsiteMeta' objects (there should only really be one)
	num_website_metas = len(WebsiteMeta.objects.all())
	if (num_website_metas == 0):
		print("No WebsiteMeta object found, creating a new one.")
		wm = WebsiteMeta()
		wm.save()
	elif(num_website_metas != 1):
		#We should only ever have one max, so if there's more than 1 raise an error
		raise Exception("More than one WebsiteMeta object found, only 1 should exist at a time. Please let Emmanuel know about this!")

#Function to get or set the total tasks ever made by the website. Uses the 'WebsiteMeta' database entry to keep track of this
def total_tasks_ever_made(increment = 0):
	check_websitemeta() #Make sure we have a websitemeta object to work with
	wm = WebsiteMeta.objects.all()[0] #Get the first (and only) WebsiteMeta object from our database
	wm.total_tasks_created += increment
	wm.save()
	return wm.total_tasks_created