"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest
from app.forms import ChamadosForm, Area_TecnicaForm

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def users(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/users.html',
        {
            'title':'Usuarios',
            'message':'Listagem de Usuarios',
            'year':datetime.now().year,
        }
    )

def addusers(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/addusers.html',
        {
            'title':'Adicionar Usuario',
            'message':'Criacao de Usuario',
            'year':datetime.now().year
        }
    )

def addchamados(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)

    form = ChamadosForm()
    if request.method == 'POST':
       form = ChamadosForm(request.POST)
       if form.is_valid():
            form.save()
            return redirect('addchamados')

    return render(
        request,
        'app/addchamados.html',
        {
            'title':'Criar um Chamado',
            'message':'Novo Chamado',
            'year':datetime.now().year,
            'form': form
        }
    )

def chamados(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/chamados.html',
        {
            'title':'Chamados',
            'message':'Verifique os chamados abertos ou abra um chamado clicando no botao Abrir Chamado',
            'year':datetime.now().year,
        }
    )


def addarea_tecnica(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)

    form = Area_TecnicaForm()
    if request.method == 'POST':
       form = Area_TecnicaForm(request.POST)
       if form.is_valid():
            form.save()
            return redirect('addarea_tecnica')

    return render(
        request,
        'app/addarea_tecnica.html',
        {
            'title':'Crição de area tecnica',
            'year':datetime.now().year,
            'form': form
        }
    )