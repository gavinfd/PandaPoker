from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

#from account.models import Account
from django.contrib.auth.models import User

class IndexView(generic.ListView):
	template_name = 'profiles.html'
	context_object_name = 'profiles_list'

	def get_queryset(self):
		return User.objects.order_by('first_name')
		
	

