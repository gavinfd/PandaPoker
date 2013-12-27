from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from variations.models import Variation

class IndexView(generic.ListView):
	template_name = 'list.html'
	context_object_name = 'variation_list'

	def get_queryset(self):
		return Variation.objects.order_by('-rating')[:5]
