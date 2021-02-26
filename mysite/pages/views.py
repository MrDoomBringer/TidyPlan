from django.shortcuts import render
from django.http import HttpResponse


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
