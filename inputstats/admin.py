from django.contrib import admin
from inputstats.models import Game, Player

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

admin.site.register(Player)


