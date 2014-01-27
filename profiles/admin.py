from django.contrib import admin
from django.contrib.auth.models import User

class ProfilesAdmin(admin.ModelAdmin):
	fieldsets = [
		('Name', {'fields': ['first_name']})
	]
	
	list_display = ('first_name' )
	search_fields = ['description']
	



