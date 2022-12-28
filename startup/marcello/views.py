from django.shortcuts import render

from django.http import HttpResponse
from django.urls import include



# Create your views here.

def homepage(request):
   return render(request,'marcello/home.html')

