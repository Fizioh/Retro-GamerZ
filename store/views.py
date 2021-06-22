#from django.shortcuts import render
from django.http import HttpResponse
from .models import Game, Contact, Creator, Booking
# Create your views here.

def index(request):
    games = Game.objects.filter(available=True).order_by('-created_at')[:6]
    formatted_games=["<li>{}</li>".format(game.title) for game in games]
    message = """<ul>{}</ul>""".format("\n".join(formatted_games))
    return HttpResponse(message)

def listing(request):
    games = Game.objects.filter(available=True)
    formatted_games=["<li>{}</li>".format(game.title) for game in games]
    message = """<ul>{}</ul>""".format("\n".join(formatted_games))
    return HttpResponse(message)

def detail(request, game_id):
    game = Game.objects.get(pk=game_id)
    creators = " ".join([creator.name for creator in game.creators.all()])
    message = "Le nom du jeu est {}. Il a été codé par {}".format(game.title, creators)
    return HttpResponse(message)

def search(request):
    query = request.GET.get('query')
    if not query:
        games = Game.objects.all()
    else:
        games = Game.objects.filter(title__icontains=query)
        
        if not games.exists():
            games = Game.objects.filter(name__icontains=query)

        if not games.exists():
            message = "Pas de bol ! Aucun résultat n'a été trouvé..."
        else:
            games = ["<li>{}</li>".format(game.title) for game in games]
            message = """
                Nous avons trouvé les jeux correspondant à votre requête ! Les voici :
                <ul>
                {}
                </ul>
            """.format("</i><li>".join(games))
        
    return HttpResponse(message)