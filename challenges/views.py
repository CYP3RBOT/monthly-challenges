from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

MONTHLY_CHALLENGES = {
    "january": "Eat no meat for the entire month",
    "february": "Walk for at least 20 minutes every day",
    "march": "Learn Django for at least 20 minutes every day",
    "april": "Eat no meat for the entire month",
    "may": "Walk for at least 20 minutes every day",
    "june": "Learn Django for at least 20 minutes every day",
    "july": "Eat no meat for the entire month",
    "august": "Walk for at least 20 minutes every day",
    "september": "Learn Django for at least 20 minutes every day",
    "october": "Eat no meat for the entire month",
    "november": "Walk for at least 20 minutes every day",
    "december": "Learn Django for at least 20 minutes every day",
}

# Create your views here.

def monthly_challenge_by_number(request: HttpRequest, month: int):
    try:
        forward_month = list(MONTHLY_CHALLENGES.keys())[month - 1]
        
        redirect_path = reverse("month-challenge", args=[forward_month]) #/challenges/january
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound("This month is not supported!")

def monthly_challenge(request: HttpRequest, month: str):
    try:
        challenge_text = MONTHLY_CHALLENGES[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")