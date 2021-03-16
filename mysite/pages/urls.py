from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('faq/', views.faq, name='faq'),
    path('howto/', views.howto, name='howto'),
    path('account/', views.account, name='account'),
    path('calendar/', views.calendar, name='calendar'),
    path('tos/', views.tos, name='tos'),
    path("create/", views.create, name = "create"),
]
