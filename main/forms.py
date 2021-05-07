from django import forms
from . import models

class SearchForm(forms.ModelForm):
    class Meta:
        model = models.Search
        fields = ('req',)
        widgets = {
            'req': forms.TextInput(attrs={'class': 'form-control mt-0', 
            'placeholder': 'Попробуй написать "Программист"',
            }),
        }