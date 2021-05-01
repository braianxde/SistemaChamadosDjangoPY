"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from app.models import Chamado, Usuario, AreaTecnica, Tecnico, Equipamento
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

class AreaTecnicaForm(forms.ModelForm):
    class Meta:
        model = AreaTecnica
        fields = ['area_tec']
        widgets = {
            'area_tec' : forms.TextInput(attrs={'class': 'form-control'})}

class TecnicoForm(forms.ModelForm):
    class Meta: 
        model = Tecnico
        fields = ['nome', 'id_area_tec', 'id_usuario']
        widgets = {
            'nome' : forms.TextInput(attrs={'class':'form-control'}),
            'id_area_tec' : forms.Select(choices = AreaTecnica.objects.values_list('id_area_tec', 'area_tec'), attrs={'class': 'form-control'}),
            'id_usuario' : forms.Select(choices = Usuario.objects.values_list('id_usuario', 'nome'), attrs={'class': 'form-control'})}

class EquipamentosForm(forms.ModelForm):
    class Meta:
        model = Equipamento 
        fields = ['nome','patrimonio','descricao']
        widgets = {            
            'nome' : forms.TextInput(attrs={'class':'form-control'}), 
            'patrimonio' : forms.TextInput(attrs={'class': 'form-control'}),
            'descricao' : forms.Textarea(attrs={'class':'form-control'})}