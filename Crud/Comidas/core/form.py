from django import forms
from django.forms import ModelForm
from .models import Comida

class ComidaForm(ModelForm):
    class Meta:
        model=Comida
        fields="__all__"
        widgets={
            'nombre':forms.TextInput(
                attrs={
                    'placeholder':'Debe ingresar un nombre',
                    'class':'form-control'
                }
            ),
            'tipo':forms.Select(
                attrs={
                    'class':'form-control'
                }
            ),
            'descripcion':forms.TextInput(
                attrs={
                    'placeholder':'Debe ingresar una descripcion ',
                    'class':'form-control',
                }
            ),
            'precio':forms.TextInput(
                attrs={
                    'placeholder':'Debe ingresar un precio',
                    'class':'form-control'
                }
            ),
        }