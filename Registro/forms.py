from django import forms
from .models import Equipo, Jugador
from django.db import models

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['nombre', 'pais']
        labels = {
            'nombre': 'Nombre',
            'pais' : 'Pais'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'pais' : forms.TextInput(attrs={'class':'form-control'}),   
        }

class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = ['nombre','apellido','edad','año','equipo']
        labels = {
            'nombre' : 'Nombre',
            'apellido': 'Apellido',
            'edad': 'Edad',
            'año' : 'Año',
            'equipo' : 'Equipo'
        }
        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'apellido' : forms.TextInput(attrs={'class':'form-control'}),
            'edad' : forms.TextInput(attrs={'class' : 'form-control'}),
            'año' : forms.TextInput(attrs={'class' : 'form-control'}),
            'equipo': forms.Select(attrs={'class': 'form-control'}),
        }