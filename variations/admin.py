from django.contrib import admin
from variations.models import Variation


class VariationAdmin(admin.ModelAdmin):
	fieldsets = [
		('Name',               {'fields': ['name']}),
		('Rating', {'fields': ['rating']}),
		('Description', {'fields': ['description']}),
	]
	
	list_display = ('name' , 'rating', 'description')
	search_fields = ['description']
	
admin.site.register(Variation, VariationAdmin)



