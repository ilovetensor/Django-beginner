from django.urls import path, include
from django.contrib import admin
from django.http import HttpResponse
from . import views
def hello(request):
    return HttpResponse("iauhdfoihsifd")

urlpatterns = [
    path("marcello/",views.homepage, name="homepage")
]
