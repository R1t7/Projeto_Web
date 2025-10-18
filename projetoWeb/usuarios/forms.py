from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class UsuarioRegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'first_name', 'last_name', 
                 'telefone', 'instituicao_ensino', 'perfil', 
                 'password1', 'password2']
        widgets = {
            'telefone': forms.TextInput(attrs={'placeholder': '(00) 00000-0000'}),
            'instituicao_ensino': forms.TextInput(attrs={'placeholder': 'Nome da Instituição'}),
            'perfil': forms.Select(attrs={'class': 'form-select'}),
        }

class LoginForm(forms.Form):
    username = forms.CharField(label='Usuário')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)

