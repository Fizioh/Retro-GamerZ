from django.shortcuts import render
from .models import Game, Contact, Creator, Booking
# Create your views here.

def index(request):
    games = Game.objects.order_by('-created_at')[:9]
    context = {'games': games}
    return render(request, 'store/index.html', context)

def listing(request):
    games = Game.objects.filter(available=True)
    context = {'games': games}
    return render(request, 'store/listing.html', context)

def detail(request, game_id):
    game = Game.objects.get(pk=game_id)
    creators_name = " ".join([creator.name for creator in game.creators.all()])
    context = {
        'game_title': game.title,
        'creators_name': creators_name,
        'game_id': game.id,
        'thumbnail': game.picture
    }
    return render(request, 'store/detail.html', context)

def search(request):
    query = request.GET.get('query')
    if not query:
        games = Game.objects.all()
    else:
        games = Game.objects.filter(title__icontains=query)
        
    if not games.exists():
        games = Game.objects.filter(creators__name__icontains=query)

    title = "Résultats pour la requête %s"%query

    context = {
        'games': games,
        'title': title,
    }
        
    return render(request, 'store/search.html', context)