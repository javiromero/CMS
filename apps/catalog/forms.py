# -*- coding: utf-8 -*-

'''
    Javier Romero Blanco
    javi.azuaga@gmail.com
    http://barrabarra.es
    ©2010
'''

from django import forms
from django.forms.models import BaseInlineFormSet
from django.forms.util import ErrorList
from django.utils.translation import ugettext as _
from catalog.models import *

class ConfigModelForm(forms.ModelForm):
    """
      Config Modelform to check if there is no other instance before saving
    """
    def clean(self):
	config = Config.objects.all()
        if config.exists() and not self.initial:
            self._errors.setdefault('__all__', ErrorList()).append("Ya existe una configuración. Para hacer cambios edite la existente.")
        return self.cleaned_data


class CategoryAdminForm(forms.ModelForm):
  """
    Formulario para comprobar que no se intentan guardar dos categorías en el mismo nivel/con mismo padre
  """
  def clean_slug(self):
      #comprobar si parent == None que self.slug no existe ya
      #unique_together(("slug", "parent"),) no tiene en cuenta que parent sea None :-( 

      data = self.cleaned_data['slug']
      parent = getattr(self.data, 'parent', None) # tomamos el atributo parent y lo ponemos a None si es vacío para poder compararlo

      # el problema es que unique_together no funciona para parent = None ¿no?
      # pues entonces vamos a comprobar solo para esos casos :D
      if parent == None:
	  categories = Category.objects.filter(slug=data, parent=parent)
	  if categories.exists() and not self.initial:
	      raise forms.ValidationError(_(u'Ya existe una categoría con esta Categoría superior y esta Ruta url'))
      
      return data 


class RequireOneFormSet(BaseInlineFormSet):
    """Require at least one form in the formset to be completed."""
    def clean(self):
        """Check that at least one form has been completed."""
        super(RequireOneFormSet, self).clean()
        for error in self.errors:
            if error:
                return
        completed = 0
        for cleaned_data in self.cleaned_data:
            # form has data and we aren't deleting it.
            if cleaned_data and not cleaned_data.get('DELETE', False):
                completed += 1

        if completed < 1:
            raise forms.ValidationError("At least one %s is required." %
                self.model._meta.object_name.lower())
