from django.test import TestCase
from django.urls import reverse

from .models import Game, Creator, Contact, Booking


class IndexPageTestCase(TestCase):
    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

class DetailPageTestCase(TestCase):
    def test_detail_page_returns_200(self):
        gta = Game.objects.create(title="GTA V")
        game_id = Game.objects.get(title='GTA V').id
        response = self.client.get(reverse('store:detail', args=(game_id, )))
        self.assertEqual(response.status_code, 200)

    def test_detail_page_returns_404(self):
        gta = Game.objects.create(title="GTA V")
        game_id = Game.objects.get(title='GTA V').id +1
        response = self.client.get(reverse('store:detail', args=(game_id, )))
        self.assertEqual(response.status_code, 404)
    
class BookingPageTestCase(TestCase):
    def setUp(self):
        Contact.objects.create(name="Markus",
        email ="markus@markus-app.fr")
        gta = Game.objects.create(title="GTA V")
        imran = Creator.objects.create(name="Imran Sarwar")
        gta.creators.add(imran)
        self.contact = Contact.objects.get(name='Markus')
        self.game = Game.objects.get(title='GTA V')
    
    def test_new_booking_is_registered(self):
        old_bookings = Booking.objects.count()
        game_id = self.game.id
        name = self.contact.name
        email = self.contact.email
        response = self.client.post(reverse('store:detail', 
        args=(game_id,)), {
            'name': name,
            'email': email
        })
        new_bookings = Booking.objects.count()
        self.assertEqual(new_bookings, old_bookings +1)