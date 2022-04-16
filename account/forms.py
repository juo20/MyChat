from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate

from account.models import Account

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
            max_length=60,
            widget=forms.TextInput(attrs={'placeholder':'Email'})
    )
    username = forms.CharField(
            widget=forms.TextInput(attrs={'placeholder':'Username'})
    )
    password1 = forms.CharField(
        widget=forms.TextInput(attrs={'type':'password', 'placeholder':'Password'})
    )
    password2 = forms.CharField(
        widget=forms.TextInput(attrs={'type':'password', 'placeholder':'Password confirm'})
    )


    class Meta:
        model = Account
        fields = ['email', 'username', 'password1', 'password2']

class AuthForm(forms.ModelForm):
    email = forms.EmailField(
            max_length=60,
            widget=forms.TextInput(attrs={'placeholder':'Email'})
    )
    password = forms.CharField(
        widget=forms.TextInput(attrs={'type':'password', 'placeholder':'Password'})
    )

    class Meta:
        model = Account
        fields = ['email', 'password']

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data.get('email')
            password = self.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if not user or not user.is_active:
                raise forms.ValidationError('User is inactive')
            return self.cleaned_data

