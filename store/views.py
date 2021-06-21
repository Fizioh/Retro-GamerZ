#from django.shortcuts import render
from django.http import HttpResponse
from .models import GAMES
# Create your views here.

def index(request):
    message = "Ohayo mina-san !"
    return HttpResponse(message)

def listing(request):
    games = ["<li>{}</li>".format(game['name']) for game in GAMES]
    message = """<ul>{}</ul>""".format("\n".join(games))
    return HttpResponse(message)

