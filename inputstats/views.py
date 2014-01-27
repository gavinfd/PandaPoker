from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.utils import simplejson
import json

from django.contrib.auth.models import User
from inputstats.models import Game, Player

class IndexView(generic.ListView):
	template_name = 'stats.html'
	context_object_name = 'data_list'

	def get_queryset(self):
		
		dates = []
		full_players = []
		
		standing = []
		games = Game.objects.order_by('game_date')
		users = User.objects.order_by('first_name')
		for user in users:
			player = Player.objects.filter(player = user.id).order_by('game')
			for p in player:
				standing.append({"date": str(p.game),"temperature": p.standing})
			break;
		
		for game in games:
			dates.append(game.game_date.strftime("%Y%m%d"))
			players = Player.objects.filter(game_id__exact = game).values_list('player', 'standing')#
			full_players.append(players)
		return json.dumps(standing, full_players)		
		'''
		poll_results = [4, 6, 7, 1]
		poll_as_json = json.dumps(poll_results)
		# Gives you a string '[4, 6, 7, 1]'

		response_data = {}
		response_data['date'] = [20111001, 20111002, 20111003, 20111004, 20111005, 20111006]
		response_data['newyork'] = [60, 61, 62, 63, 64, 65]
		response_data['sanfran'] = [41, 43, 42, 49, 42, 50]
		response_data['austin'] = [50, 55, 52, 53, 51, 58]
		
		data_as_json = json.dumps(response_data)
		#return HttpResponse(json.dumps(response_data), content_type="application/json")
		
		#return poll_as_json
		return data_as_json
		'''
	'''
	def my_ajax_view(request):
		if not request.is_ajax():
			raise Http404
	
		response_data = {}
		response_data['date'] = [20111001, 20111002, 20111003, 20111004, 20111005, 20111006]
		response_data['newyork'] = [60, 61, 62, 63, 64, 65]
		response_data['sanfran'] = [41, 43, 42, 49, 42, 50]
		response_data['austin'] = [50, 55, 52, 53, 51, 58]
		
		data_dict = getmydata() #lets supose is a dict
		return HttpResponse(simplejson.dumps(response_data))
	'''
class DetailView(generic.DetailView):
	model = Game
	template_name = 'detail.html'

class PlayerInfoView(generic.DetailView):
	model = Player
	template_name = 'playerinfo.html'
	
	def playerinfo(self, request, *args, **kwargs):
		if kwargs.get('pk', None):
			return None

class ResultsView(generic.DetailView):
	model = Game
	template_name = 'results.html'
'''
def vote(request, question_id):
	p = get_object_or_404(Game, pk=question_id)
	try:
		player = p.player_set.get(pk=request.POST['game.id'])
	except (KeyError, Player.DoesNotExist):
		# Redisplay the question voting form.
		return render(request, 'detail.html', {
			'question': p,
			'error_message': "You didn't select a choice.",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
		# with POST data. This prevents data from being posted twice if a
		# user hits the Back button.
		return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
'''