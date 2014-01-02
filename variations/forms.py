from django import forms
from variations.models import Variation

class VariationForm(forms.ModelForm):
    
    class Meta:
        model = Variation
        
    def save_variation(self):
        pass