from django.db import models

# Create your models here.

class Creator(models.Model):
    name = models.CharField(max_length=200, unique=True)

class Contact(models.Model):
    email = models.EmailField(max_length=100)
    name = models.CharField(max_length=200)

class Game(models.Model):
    reference = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)
    title = models.CharField(max_length=200)
    picture= models.URLField()
    creators = models.ManyToManyField(Creator, related_name='games', blank=True)

class Booking(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    contacted = models.BooleanField(default=False)
    game = models.OneToOneField(Game, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)




