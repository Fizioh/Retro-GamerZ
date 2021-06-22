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

def detail(request, game_id):
    id = int(game_id)
    game = GAMES[id]
    creators = " ".join([creator['name'] for creator in game['creators']])
    message = "Le nom du jeu est {}. Il a été codé par {}".format(game['name'], creators)
    return HttpResponse(message)

def search(request):
    query = request.GET.get('query')
    if not query:
        message = "Aucun créateur n'est demandé"
    else:
        games = [
            game for game in GAMES
            if query in " ".join(creator['name'] for creator in game['creators'])
        ]
        
        if len(games) == 0:
            message = "Pas de bol ! Il n'y a aucun résultat..."
        else:
            games = ["<li>{}</li>".format(game['name']) for game in games]
            message = """
                Nous avons trouvé les eux correspondant à votre requête ! Les voici :
                <ul>
                {}
                </ul>
            """.format("</i><li>".join(games))
        
    return HttpResponse(message)