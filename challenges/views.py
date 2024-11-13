from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound

# Create your views here.

def monthly_challenge(request: HttpRequest, month: str):
    challenge_text = None
    
    if month == "january":
        challenge_text = "Eat no meat for the entire month"
    elif month == "february":
        challenge_text = "Walk for at least 20 minutes every day"
    elif month == "march":
        challenge_text = "Learn Django for at least 20 minutes every day"
    else:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(challenge_text)