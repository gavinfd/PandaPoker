from django.shortcuts import get_object_or_404, render, render_to_response
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.generic.edit import FormView

from variations.forms import VariationForm
from inputstats.models import Game
from variations.models import Variation
import operator

class IndexView(generic.ListView):
	template_name = 'list.html'
	context_object_name = 'variation_list'

	def get_queryset(self):
		games = Game.objects.values_list('variation', flat=True).order_by('variation')
		
		list = []
		variations = Variation.objects.all()
		for variation in variations:
			variation.times_played = Game.objects.filter(variation_id = variation).count()
			list.append(variation)
		list.sort(key=operator.attrgetter('times_played'), reverse=True)
		return list
	
	
class AddView(FormView):
	template_name = 'add_variation.html'
	form_class = VariationForm
	success_url =""
	fields = ['name']
	
def outline(request):
	name = request.POST.get("name")
	description = request.POST.get("description")
	v = Variation(name=name, description=description, rating=0)
	v.save()
	return  render_to_response('list.html', {'name':name, 'description':description})