from films.models import Film
from django import forms
import datetime

class FilmForm(forms.ModelForm):
    
    #year = forms.forms.DateField(initial=datetime.date.today)
    year = forms.CharField(widget = forms.TextInput(),help_text='*25 characters max.')
    class Meta:
        model = Film
        exclude = ['display']
        #fields = ('film_name','year','rate')