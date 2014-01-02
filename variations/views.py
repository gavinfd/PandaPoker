from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.generic.edit import FormView

from variations.forms import VariationForm
from variations.models import Variation

class IndexView(generic.ListView):
	template_name = 'list.html'
	context_object_name = 'variation_list'

	def get_queryset(self):
		return Variation.objects.order_by('-rating')[:5]
	
class AddView(FormView):
	template_name = 'add_variation.html'
	form_class = VariationForm
	success_url =""
	fields = ['name']
	
	def add(self, form):
		form.save_variation()
		return super(AddView, self).form_valid(form)