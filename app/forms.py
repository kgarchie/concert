from django.contrib.auth.models import User
from django import forms


class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
