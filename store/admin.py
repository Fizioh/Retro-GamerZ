from django.contrib import admin
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType

from .models import Booking, Contact, Creator, Game


class AdminURLMixin(object):
    def get_admin_url(self, obj):
        content_type = ContentType.objects.get_for_model(obj.__class__)
        return reverse("admin:store_%s_change" % (
            content_type.model),
            args=(obj.id,))


class BookingInLine(admin.TabularInline, AdminURLMixin):
    model = Booking
    readonly_fields = ['created_at', 'contacted',  'game_link']
    fieldsets = [
        (None, {'fields': ['created_at', 'game_link', 'contacted']})
        ]
    extra = 0
    verbose_name = "Réservation"
    verbose_name_plural = "Réservations"

    def game_link(self, booking):
        url = self.get_admin_url(booking.game)
        return mark_safe("<a href='{}'>{}</a>".format(url, booking.game.title))


class GameCreatorInline(admin.TabularInline):
    model = Game.creators.through
    extra = 1
    

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    inlines = [BookingInLine, ]

@admin.register(Creator)
class CreatorAdmin(admin.ModelAdmin):
    inlines = [GameCreatorInline, ]

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    search_fields = ['reference', 'title']
    fieldsets = [
        (None, {'fields': ['title', 'available']})
        ]

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin, AdminURLMixin):
    list_filter = ['created_at', 'contacted']
    readonly_fields = ['created_at', 'contact_link', 'game_link', 'contacted']
    fields = ['created_at', 'game_link', 'contacted', 'contact_link']


    def game_link(self, booking):
        url = self.get_admin_url(booking.game)
        return mark_safe("<a href='{}'>{}</a>".format(url, booking.game.title))

    def contact_link(self, booking):
        url = self.get_admin_url(booking.contact)
        return mark_safe("<a href='{}'>{}</a>".format(url, booking.contact.name))