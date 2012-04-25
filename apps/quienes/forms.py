# -*- coding: utf-8 -*-
# coding=UTF-8
'''
    Sempatiza

    Desarrollado por Lastchance SL
    web: www.lastchance.es
    email: jao@lastchance.es
    Fecha: 2010
'''
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.localflavor.es.forms import ESPhoneNumberField
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import RequestContext, Template, loader
from django.template.loader import render_to_string

class Contacto(forms.Form):
    '''
    Formulario de Contacto
    '''
    #HORARIO_CHOICES = (
        #('', 'Selecciona horario'),
        #('Mañanas', 'Mañanas'),
        #('Tardes', 'Tardes'),
        #('Indiferente', 'Indiferente'),
    #)

    nombre = forms.CharField(min_length=3, label='Nombre', widget=forms.TextInput(attrs={'class':'span-3 text'}))
    telefono = ESPhoneNumberField(label='Teléfono', widget=forms.TextInput(attrs={'class':'span-3 text'}))
    correo = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class':'span-3 text'}))
    #horario = forms.ChoiceField(choices=HORARIO_CHOICES, label='Horario', widget=forms.Select(attrs={'class':'span-3'}))