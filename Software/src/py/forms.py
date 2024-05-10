from django import forms
from ..src.py.models import Carro


class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario', max_length=100)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

class CarroForm(forms.ModelForm):
    class Meta:
        model = Carro
        fields = ['marca', 'modelo', 'año', 'transmision']