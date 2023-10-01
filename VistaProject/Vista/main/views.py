from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
# Create your views here.

def intro_view(request: HttpRequest):

    return render(request, "main/home.html")


def service_view(request: HttpRequest):

    return render(request, "main/service.html")

