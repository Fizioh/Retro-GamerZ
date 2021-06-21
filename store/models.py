#from django.db import models

# Create your models here.

CREATORS = {
    'michel-ancel': {'name': 'Michel Ancel'},
    'koji-kondo': {'name': 'Koji Kondo'},
    'jade-raymond': {'name': 'Jade Raymond'}

}

GAMES = [
    {'name': 'Rayman', 'creators': [CREATORS['michel-ancel']]},
    {'name': 'Zelda', 'creators': [CREATORS['koji-kondo']]},
    {'name': 'Assasins Creed', 'creators': [CREATORS['jade-raymond']]}
]