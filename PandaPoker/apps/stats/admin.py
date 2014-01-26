from django.contrib import admin
from apps.stats.models import Game, Player, Hand
from django.contrib.auth.models import User
from apps.variations.models import Variation

class PlayerInline(admin.TabularInline):
	model = Player
	extra = 3

class GameAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,               {'fields': ['variation']}),
		('Date information', {'fields': ['game_date'],
								'classes': ['collapse']}),
	]
	
	list_display = ('variation' , 'game_date')
	inlines = [PlayerInline]
	list_filter =['game_date']
	search_fields = ['variation']
	
admin.site.register(Game, GameAdmin)

class PlayerAdmin(admin.ModelAdmin):
	fieldsets = [
		('Game',               {'fields': ['game']}),
		('Player', 				{'fields': ['player']}),
		('Standing',               {'fields': ['standing']}),
		('Knockouts',               {'fields': ['knockouts']}),
		('Highest Hand',               {'fields': ['highesthand']})
	]
	
	list_display = ('game' , 'player', 'standing', 'knockouts', 'highesthand')
	list_filter =['game', 'player']
	search_fields = ['player']

admin.site.register(Player, PlayerAdmin)

class HandAdmin(admin.ModelAdmin):
	fieldsets = [
		('Cards',               {'fields': ['cards']}),
		('Description', 		{'fields': ['description']}),

	]
	
	list_display = ('cards' , 'description')

admin.site.register(Hand, HandAdmin)


