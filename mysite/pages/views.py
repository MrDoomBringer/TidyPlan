from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
from .forms import CreateNewList


def index(request):
    return HttpResponse("Home Page")

def faq(request):
    return HttpResponse("FAQ")

def howto(request):
    return HttpResponse("How To")

def account(request):
    return HttpResponse("Account Page")

def calendar(request):
    return HttpResponse("Calendar")

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
