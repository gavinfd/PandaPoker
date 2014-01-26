from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import simplejson
import json

from django.contrib.auth.models import User
from apps.stats.models import Game, Player

class IndexView(generic.ListView):
    template_name = 'stats.html'
    context_object_name = 'data_list'

    def get_queryset(self):
        return None
        
        '''
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