from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def quotes(request):
    quotes_list = [
        "Felieve in yoursled.",
        "push your limits."
        "Stay consistent.",
        "Dream bad.",
        "Success is not accident."
    ]

    random_quote = random.choice(quotes_list)
    data = {}
    data['quote'] = random_quote
    data['all_quotes'] = quotes_list
    return render(request, 'app/quotes.html')
