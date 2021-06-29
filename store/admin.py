from django.contrib import admin

from .models import Booking, Contact, Creator, Game



class BookingInLine(admin.TabularInline):
    model = Booking
    fieldsets = [
        (None, {'fields': ['game', 'contacted']})
        ]
    extra = 0


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
class BookingAdmin(admin.ModelAdmin):
    list_filter = ['created_at', 'contacted']
