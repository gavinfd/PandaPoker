from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.db.models import Count, Sum, Avg

#from account.models import Account
from django.contrib.auth.models import User
from inputstats.models import Player
from inputstats.models import Game
import operator

class IndexView(generic.ListView):
	template_name = 'profiles.html'
	context_object_name = 'profiles_list'

	def get_queryset(self):
		
		full_players = []
		players = {}
		users = User.objects.order_by('first_name')
		players = Player.objects.order_by('player', '-highesthand').annotate(total_knockouts=Sum("knockouts"))
		
		for user in users:
			players = Player.objects.filter(player_id__exact = user.id).order_by('highesthand').annotate(total_knockouts=Sum("knockouts"))
			if players:
				
				current = players[0]
				current.average_standing = 0
				for player in players:
					current.average_standing += player.standing
				current.games_played = len(players)
				current.average_standing = float(current.average_standing)/float(current.games_played)
				full_players.append(current)
		full_players.sort(key=operator.attrgetter('average_standing'), reverse=False)
		return full_players