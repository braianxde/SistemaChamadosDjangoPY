"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from app.models import Chamado, Usuario, Tecnico, Area_tec
from django.db import models
from django.utils.translation import ugettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class ChamadosForm(forms.ModelForm):
    class Meta:
        model = Chamado
        fields = ['assunto', 'texto', 'data_abertura', 'status', 'id_usuario']
        widgets = {
            'assunto' : forms.TextInput(attrs={'class': 'form-control'}),
            'texto' : forms.Textarea(attrs={'class': 'form-control'}),
            'data_abertura' : forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'status' : forms.Select(attrs={'class': 'form-control'}),
            'id_usuario' : forms.Select(choices = Usuario.objects.values_list('id_usuario', 'nome'), attrs={'class': 'form-control'})}

class TecnicoForm(forms.ModelForm):
    class Meta: 
        model = Tecnico
        fields = ['nome', 'data_criacao', 'id_area_tec', 'id_usuario']
        widgets = {
            'nome' : forms.CharField(max_length=45),
            'data_criacao' : forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'id_area_tec' : forms.Select(choices = Area_tec.objects.values_list('id_area_tec', 'nome'), attrs={'class': 'form-control'}),
            'id_usuario' : forms.Select(choices = Usuario.objects.values_list('id_usuario', 'nome'), attrs={'class': 'form-control'})}