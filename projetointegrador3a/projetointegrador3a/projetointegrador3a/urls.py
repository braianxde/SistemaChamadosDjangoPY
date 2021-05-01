"""
Definition of urls for projetointegrador3a.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('users/', views.users, name='users'),
    path('chamados/', views.chamados, name='chamados'),
    path('areastecnicas/', views.areastecnicas, name='areastecnicas'),
    path('equipamentos/', views.equipamentos, name='equipamentos'),
    path('tecnicos/', views.tecnicos, name='tecnicos'),
    path('addchamados/', views.addchamados, name='addchamados'),
    path('addareatecnica/', views.addareatecnica, name='addareatecnica'),
    path('addequipamentos/', views.addequipamentos, name='addequipamentos'),
    path('addtecnicos/', views.addtecnicos, name='addtecnicos'),
    path('addusers/', views.addusers, name='addusers'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]
