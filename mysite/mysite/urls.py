from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('admin/', admin.site.urls),
	path("<str:name_text>",views.index, name = "index"),
	path("",views.home,name ="home"),
]