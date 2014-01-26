from apps.variations.models import Variation
from django.contrib import admin

class VariationAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name',               {'fields': ['name']}),
        ('Description', {'fields': ['description']}),
    ]
    
    list_display = ('name' , 'description')
    search_fields = ['description']
    
admin.site.register(Variation, VariationAdmin)
