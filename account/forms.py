from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate

from account.models import Account

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required email address')

    class Meta:
        model = Account
        fields = ["email", "username", "is_admin", "password1", "password2"]

# Tried to overwrite AuthenticationForm but its not really working yet
class AuthForm(forms.ModelForm):
    password = forms.CharField(max_length=60, help_text='Enter pw')

    class Meta:
        model = Account
        fields = ["email", "password"]

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data.get('email')
            password = self.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if not user or not user.is_active:
                raise forms.ValidationError("lmao")
            #return self.cleaned_data

