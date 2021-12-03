from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
  "january": "Eat Vegetables Because You Hate Them Make Them Extinct Kids!",
  "febuary": "Work Out For At Least Two Hours Every Day! Tip: Get Strong",
  "march": "Learn Django And Python For At Least 3 Hours Every Day!",
  "april": "Eat Vegetables Because You Hate Them Make Them Extinct Kids!",
  "may": "Work Out For At Least Two Hours Every Day! Tip: Get Strong",
  "june":"Learn Django And Python For At Least 3 Hours Every Day!",
  "july" : "Eat Vegetables Because You Hate Them Make Them Extinct Kids!",
  "august": "Work Out For At Least Two Hours Every Day! Tip: Get Strong",
  "september": "Learn Django And Python For At Least 3 Hours Every Day!",
  "october": "Eat Vegetables Because You Hate Them Make Them Extinct Kids!",
  "november": "Work Out For At Least Two Hours Every Day! Tip: Get Strong",
  "december": "Learn Django And Python For At Least 3 Hours Every Day!",
}

# Create your views here.

def index(request):
  list_items = ""
  months = list(monthly_challenges.keys())

  for month in months:
    capitalized_month = month.capitalize()
    month_path = reverse("month-challenge", args=[month])
    list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

# "<li><a href="...">January</a></li><li><a href="...">Febuary</a></li>..."

  response_data = f"<ul>{list_items}</ul>"   
  return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
  months = list(monthly_challenges.keys())

  if month > len(months):
      return HttpResponseNotFound("Invalid month")

  redirect_month = months[month - 1]
  redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenge/january
  return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
      challenge_text = monthly_challenges[month]
      response_data = f"<h1>{challenge_text}</h1>"
      return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
    