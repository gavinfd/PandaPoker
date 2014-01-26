from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.db.models import Count, Sum, Avg

from django.contrib.auth.models import User
from apps.stats.models import Player, Game
import operator

class IndexView(generic.ListView):
    template_name = 'payouts.html'
    context_object_name = 'payouts_list'
    
    def get_queryset(self):
        return None