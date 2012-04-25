# -*- coding: utf-8 -*-
'''
    Javier Romero

    Desarrollado por Barrabarra
    web: http://barrabarra.es
    email: javi@barrabarra.es
    Fecha: 2011
'''

from django import forms
from django.forms.util import ErrorList
from django.utils.translation import ugettext_lazy as _
from contact.models import *

class ContactModelForm(forms.ModelForm):
    """
    Render a Contact modelform and check if there is more than 1 instance in the db before saving
    """

    class Meta:
	model = ContactConfig

    def clean(self):
	contact = ContactConfig.objects.all()
	if contact.exists() and not self.initial:
            self._errors.setdefault('__all__', ErrorList()).append(_('Ya existe una configuración para los formularios de contacto. Por favor edítela para hacer cambios.'))
        return self.cleaned_data  

class ContactForm(forms.ModelForm):
    """
    Render a contact form
    """
    attrs = {'class': 'input_text'}
    attrs_req = {'class': 'input_text required'}
    
    nombre      = forms.CharField(label=u'Nombre', required=True, widget=forms.TextInput(attrs={'onfocus': 'clearTextName(this)', 'onblur': 'setTextName(this)'}))
    email       = forms.CharField(label=u'Correo Electrónico', required=True, widget=forms.TextInput(attrs={'onfocus': 'clearTextEmail(this)', 'onblur': 'setTextEmail(this)'}))
    phone_number= forms.CharField(label=u'Teléfono', required=False, widget=forms.TextInput(attrs={'onfocus': 'clearTextPhone(this)', 'onblur': 'setTextPhone(this)'}))
    mensaje     = forms.CharField(label=u'Me gustaría saber más información acerca de...', required=True, min_length=25, widget=forms.Textarea(attrs={'onfocus': 'clearTextMsg(this)', 'onblur': 'setTextMsg(this)'}))
    condiciones = forms.BooleanField(label=u'He leído el <a href="/aviso-legal/" target="_blank">Aviso legal</a>', required=True)
    
    class Meta:
	model = Message
	exclude = ('fecha', 'ip',)

class ContactmeForm(forms.ModelForm):
    """
    Render a contact form
    """
    attrs = {'class': 'input_text'}
    attrs_req = {'class': 'input_text required'}
    
    nombre      = forms.CharField(label=u'Nombre', required=True, widget=forms.TextInput(attrs={'onfocus': 'clearTextName(this)', 'onblur': 'setTextName(this)'}))
    telefono    = forms.CharField(label=u'Teléfono', required=False, widget=forms.TextInput(attrs={'onfocus': 'clearTextPhone(this)', 'onblur': 'setTextPhone(this)'}))
    email       = forms.CharField(label=u'Correo Electrónico', required=True, widget=forms.TextInput(attrs={'onfocus': 'clearTextEmail(this)', 'onblur': 'setTextEmail(this)'}))
    mensaje     = forms.CharField(label=u'Me gustaría saber más información acerca de...', required=True, widget=forms.Textarea(attrs={'onfocus': 'clearTextMsg(this)', 'onblur': 'setTextMsg(this)'}))
    condiciones = forms.BooleanField(label=u'He leído el <a href="/aviso-legal/" target="_blank">Aviso legal</a>', required=True)
    
    class Meta:
	model = Message
	exclude = ('fecha', 'ip',)
