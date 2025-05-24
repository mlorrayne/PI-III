from django import forms
from .models import Apoio, Voluntariado

class ApoioForm(forms.ModelForm):
    class Meta:
        model = Apoio
        fields = ['nome', 'email', 'mensagem']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'mensagem': forms.Textarea(attrs={'class': 'form-control'}),
        }

class VoluntariadoForm(forms.ModelForm):
    class Meta:
        model = Voluntariado
        fields = ['nome', 'telefone', 'email', 'disponibilidade']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:600px;'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:600px;'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'style': 'width:600px;'}),
            'disponibilidade': forms.Textarea(attrs={'class': 'form-control'}),
        }
