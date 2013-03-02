#!/usr/bin/env python

from django.contrib import admin
from team.models import Roster, Players

class RosterAdmin(admin.ModelAdmin):
    search_fields = ('name',)

admin.site.register(Roster, RosterAdmin)

class PlayersAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    
admin.site.register(Players, PlayersAdmin)

