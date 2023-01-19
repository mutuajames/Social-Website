from django import forms 
from django.contrib.auth.models import User


class LoginForm(forms.Form):
  username = forms.CharField()
  password = forms.CharField(widget=forms.PasswordInput)

  
class RegistrationForm(forms.ModelForm):
  password = forms.CharField(label='Password', widget=forms.PasswordInput)
  password1 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

  class Meta:
    Model = User
    fields = ['username', 'first_name','email']

  def clean_password2(self):
    cd = self.cleaned_data
    if cd['password'] != cd['password2']:
      raise forms.ValidationError('Passwords don\'t match.')
    return cd['password2']
    