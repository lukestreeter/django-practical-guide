from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
  "january": "𝐸𝒶𝓉 𝒱𝑒𝑔𝑒𝓉𝒶𝒷𝓁𝑒𝓈 𝐵𝑒𝒸𝒶𝓊𝓈𝑒 𝒴𝑜𝓊 𝐻𝒶𝓉𝑒 𝒯𝒽𝑒𝓂 𝑀𝒶𝓀𝑒 𝒯𝒽𝑒𝓂 𝐸𝓍𝓉𝒾𝓃𝒸𝓉 𝒦𝒾𝒹𝓈!",
  "febuary": "𝓦𝓸𝓻𝓴 𝓞𝓾𝓽 𝓕𝓸𝓻 𝓐𝓽 𝓛𝓮𝓪𝓼𝓽 𝓣𝔀𝓸 𝓗𝓸𝓾𝓻𝓼 𝓔𝓿𝓮𝓻𝔂 𝓓𝓪𝔂! 𝓣𝓲𝓹: 𝓖𝓮𝓽 𝓢𝓽𝓻𝓸𝓷𝓰",
  "march": "𝐿𝑒𝒶𝓇𝓃 𝒟𝒿𝒶𝓃𝑔𝑜 𝒜𝓃𝒹 𝒫𝓎𝓉𝒽𝑜𝓃 𝐹𝑜𝓇 𝒜𝓉 𝐿𝑒𝒶𝓈𝓉 𝟥 𝐻𝑜𝓊𝓇𝓈 𝐸𝓋𝑒𝓇𝓎 𝒟𝒶𝓎!",
  "april": "𝐸𝒶𝓉 𝒱𝑒𝑔𝑒𝓉𝒶𝒷𝓁𝑒𝓈 𝐵𝑒𝒸𝒶𝓊𝓈𝑒 𝒴𝑜𝓊 𝐻𝒶𝓉𝑒 𝒯𝒽𝑒𝓂 𝑀𝒶𝓀𝑒 𝒯𝒽𝑒𝓂 𝐸𝓍𝓉𝒾𝓃𝒸𝓉 𝒦𝒾𝒹𝓈!",
  "may": "𝓦𝓸𝓻𝓴 𝓞𝓾𝓽 𝓕𝓸𝓻 𝓐𝓽 𝓛𝓮𝓪𝓼𝓽 𝓣𝔀𝓸 𝓗𝓸𝓾𝓻𝓼 𝓔𝓿𝓮𝓻𝔂 𝓓𝓪𝔂! 𝓣𝓲𝓹: 𝓖𝓮𝓽 𝓢𝓽𝓻𝓸𝓷𝓰",
  "june":"𝐿𝑒𝒶𝓇𝓃 𝒟𝒿𝒶𝓃𝑔𝑜 𝒜𝓃𝒹 𝒫𝓎𝓉𝒽𝑜𝓃 𝐹𝑜𝓇 𝒜𝓉 𝐿𝑒𝒶𝓈𝓉 𝟥 𝐻𝑜𝓊𝓇𝓈 𝐸𝓋𝑒𝓇𝓎 𝒟𝒶𝓎!",
  "july" : "𝐸𝒶𝓉 𝒱𝑒𝑔𝑒𝓉𝒶𝒷𝓁𝑒𝓈 𝐵𝑒𝒸𝒶𝓊𝓈𝑒 𝒴𝑜𝓊 𝐻𝒶𝓉𝑒 𝒯𝒽𝑒𝓂 𝑀𝒶𝓀𝑒 𝒯𝒽𝑒𝓂 𝐸𝓍𝓉𝒾𝓃𝒸𝓉 𝒦𝒾𝒹𝓈!",
  "august": "𝓦𝓸𝓻𝓴 𝓞𝓾𝓽 𝓕𝓸𝓻 𝓐𝓽 𝓛𝓮𝓪𝓼𝓽 𝓣𝔀𝓸 𝓗𝓸𝓾𝓻𝓼 𝓔𝓿𝓮𝓻𝔂 𝓓𝓪𝔂! 𝓣𝓲𝓹: 𝓖𝓮𝓽 𝓢𝓽𝓻𝓸𝓷𝓰",
  "september": "𝐿𝑒𝒶𝓇𝓃 𝒟𝒿𝒶𝓃𝑔𝑜 𝒜𝓃𝒹 𝒫𝓎𝓉𝒽𝑜𝓃 𝐹𝑜𝓇 𝒜𝓉 𝐿𝑒𝒶𝓈𝓉 𝟥 𝐻𝑜𝓊𝓇𝓈 𝐸𝓋𝑒𝓇𝓎 𝒟𝒶𝓎!",
  "october": "𝐸𝒶𝓉 𝒱𝑒𝑔𝑒𝓉𝒶𝒷𝓁𝑒𝓈 𝐵𝑒𝒸𝒶𝓊𝓈𝑒 𝒴𝑜𝓊 𝐻𝒶𝓉𝑒 𝒯𝒽𝑒𝓂 𝑀𝒶𝓀𝑒 𝒯𝒽𝑒𝓂 𝐸𝓍𝓉𝒾𝓃𝒸𝓉 𝒦𝒾𝒹𝓈!",
  "november": "𝓦𝓸𝓻𝓴 𝓞𝓾𝓽 𝓕𝓸𝓻 𝓐𝓽 𝓛𝓮𝓪𝓼𝓽 𝓣𝔀𝓸 𝓗𝓸𝓾𝓻𝓼 𝓔𝓿𝓮𝓻𝔂 𝓓𝓪𝔂! 𝓣𝓲𝓹: 𝓖𝓮𝓽 𝓢𝓽𝓻𝓸𝓷𝓰",
  "december": "𝐿𝑒𝒶𝓇𝓃 𝒟𝒿𝒶𝓃𝑔𝑜 𝒜𝓃𝒹 𝒫𝓎𝓉𝒽𝑜𝓃 𝐹𝑜𝓇 𝒜𝓉 𝐿𝑒𝒶𝓈𝓉 𝟥 𝐻𝑜𝓊𝓇𝓈 𝐸𝓋𝑒𝓇𝓎 𝒟𝒶𝓎!",
}

# Create your views here.

def index(request):
  months = list(monthly_challenges.keys())

  return render(request, "challenges/index.html", {
        "months": months       
    })

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
      return render(request, "challenges/challenge.html", {
        "text": challenge_text,
        "month_name": month
      })
    except:
      return HttpResponseNotFound("<h1>This month is not supported!</h1>")
  