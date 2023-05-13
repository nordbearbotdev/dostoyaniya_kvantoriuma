from django import forms
from .models import *


class LoginForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['login', 'password']
        widget = {
            'login': forms.TextInput(attrs={'class': 'form-input'}),
            'password': forms.TextInput(attrs={'class': 'form-input', type: 'password'})
        }


