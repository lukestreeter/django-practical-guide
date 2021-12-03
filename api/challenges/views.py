from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

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


        def monthly_challenge_by_number(request, month):
          months = list(monthly_challenges.keys())

          if month > len(months):
      return HttpResponseNotFound("Invalid month")

  redirect_month = months[month - 1]
  return HttpResponseRedirect("/challenges/" + redirect_month)


def monthly_challenge(request, month):
    try:
      challenge_text = monthly_challenges[month]
      return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")
    