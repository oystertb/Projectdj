from users.models import UserProfile
from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(),error_messages={'required' : 'Please enter a proper password'}) # djangonun tanimladigi password attribute hidden type degil
    password2 = forms.CharField(widget=forms.PasswordInput(),error_messages={'required' : 'Please enter a proper password'})
    username = forms.CharField(widget = forms.TextInput(),help_text='*20 characters max.') # username yaninda yazan uzun warning message i kaldirmak icin default username uzerine overwrite yaptim.

    class Meta:
        model = User
        fields = ('username', 'email', 'password','password2')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website',) # picture da vardi