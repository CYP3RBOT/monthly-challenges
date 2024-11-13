from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.

def january(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Do 10 pushups every day!")

def febuary(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Walk for at least 20 minutes every day!")