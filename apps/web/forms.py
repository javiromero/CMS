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
from django.forms.util import ErrorList
from django.utils.translation import ugettext_lazy as _
from web.models import HomePage, Pagina


class HomePageModelForm(forms.ModelForm):
    def clean(self):
        if HomePage.objects.count() > 1:
            self._errors.setdefault('__all__', ErrorList()).append("Ya existe una portada y no se pueden crear más. Edita la existente.")
        return self.cleaned_data

class PaginaAdminForm(forms.ModelForm):
  """
    Formulario para comprobar que no se intentan guardar dos páginas en el mismo nivel/con mismo padre
  """
  def clean_slug(self):
      #comprobar si parent == None que self.slug no existe ya
      #unique_together(("slug", "parent"),) no tiene en cuenta que parent sea None :-( 

      data = self.cleaned_data['slug']
      parent = getattr(self.data, 'parent', None) # tomamos el atributo parent y lo ponemos a None si es vacío para poder compararlo

      # el problema es que unique_together no funciona para parent = None ¿no?
      # pues entonces vamos a comprobar solo para esos casos :D
      if parent == None:
          pages = Pagina.objects.filter(slug=data, parent=parent)
          if pages.exists() and not self.initial:
              raise forms.ValidationError(_(u'Ya existe una página con esta Página superior y esta Ruta url'))
      
      return data 