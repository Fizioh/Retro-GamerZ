from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import transaction, IntegrityError

from .models import Game, Contact, Creator, Booking
from .forms import ContactForm, ParagraphErrorList
# Create your views here.

def index(request):
    games = Game.objects.filter(available=True).order_by('-created_at')[:4]
    context = {
        'games': games
        }
    return render(request, 'store/index.html', context)

def listing(request):
    games_list = Game.objects.order_by('-created_at')
    paginator = Paginator(games_list, 9)
    page = request.GET.get('page')
    try:
        games = paginator.page(page)
    except PageNotAnInteger:
        games = paginator.page(1)
    except EmptyPage:
        #if page is out of range (ex 999), deliver last page of results
        games = paginator.page(paginator.num_pages)
    context = {
        'games': games,
        'paginate': True
        }
    return render(request, 'store/listing.html', context)

def detail(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    creators_name = " ".join([creator.name for creator in game.creators.all()])
    context = {
        'game_title': game.title,
        'creators_name': creators_name,
        'game_id': game.id,
        'thumbnail': game.picture
    }
    if request.method == 'POST':
        form = ContactForm(request.POST, error_class=ParagraphErrorList)
        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            
            try:
                with transaction.atomic():
                    contact = Contact.objects.filter(email=email)
                    if not contact.exists():
                    # if contact is not registered create one
                        contact = Contact.objects.create(
                            email=email,
                            name=name
                        )
                    else:
                        contact = contact.first()
                    game = get_object_or_404(Game, id=game_id)
                    booking = Booking.objects.create(
                        contact=contact,
                        game=game
                    )
                    game.available = False
                    game.save()
                    context = {
                        'game_title': game.title
                    }
                    return render(request, 'store/merci.html', context)
            except IntegrityError:
                form.errors['internal'] = "Une erreur interne est survenue... Merci de recommencer votre requête."
    else:
        form = ContactForm()

    context['form'] = form
    context['errors'] = form.errors.items()
    return render(request, 'store/detail.html', context)

def search(request):
    query = request.GET.get('query')
    if not query:
        games = Game.objects.all()
    else:
        games = Game.objects.filter(title__icontains=query)
        
    if not games.exists():
        games = Game.objects.filter(creators__name__icontains=query)

    title = "Résultats pour : %s"%query

    context = {
        'games': games,
        'title': title,
    }
        
    return render(request, 'store/search.html', context)