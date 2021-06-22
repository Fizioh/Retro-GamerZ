#from django.db import models

# Create your models here.

CREATORS = {
    'michel-ancel': {'name': 'Michel Ancel'},
    'konchan': {'name': 'Koji Kondo'},
    'ibjade': {'name': 'Jade Raymond'},
    'patrice-desilets': {'name': 'Patrice Désilets'},

}

GAMES = [
    {'name': 'Rayman', 'creators': [CREATORS['michel-ancel']]},
    {'name': 'Zelda', 'creators': [CREATORS['konchan']]},
    {'name': 'Assasins Creed', 'creators': [CREATORS['ibjade'], CREATORS['patrice-desilets']]}
]