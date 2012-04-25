# -*- coding: utf-8 -*-

"""
View which can render and send email from a contact form.

"""

from django.core import urlresolvers
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import RequestContext
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _
from contact.forms import ContactForm, ContactmeForm
from contact.models import ContactConfig
from catalog.models import Product


def contact_form(request, template_name):
    """
    Renders a contact form, validates its input and sends an email
    from it.
    
    To specify the form class to use, pass the ``form_class`` keyword
    argument; if no ``form_class`` is specified, the base
    ``ContactForm`` class will be used.
    
    To specify the template to use for rendering the form (*not* the
    template used to render the email message sent from the form,
    which is handled by the form class), pass the ``template_name``
    keyword argument; if not supplied, this will default to
    ``contact_form/contact_form.html``.
    
    To specify a URL to redirect to after a successfully-sent message,
    pass the ``success_url`` keyword argument; if not supplied, this
    will default to ``/contact/sent/``.
    
    To allow only registered users to use the form, pass a ``True``
    value for the ``login_required`` keyword argument.
    
    To suppress exceptions raised during sending of the email, pass a
    ``True`` value for the ``fail_silently`` keyword argument. This is
    **not** recommended.
    
    Template::
    
        Passed in the ``template_name`` argument.
        
    Context::
    
        form
            The form instance.
    
    """
   
    try:
        current_site = Site.objects.get_current()
        contact_data = ContactConfig.objects.get()
    except ContactConfig.DoesNotExist:
        contact_data = ''

    # cool, you can try a value and fallback to another if it doesn't exist
    #page_title = getattr(contact_data, 'title', _('Contact'))

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
	    message = form.save(commit=False)
	    message.ip = request.META.get('REMOTE_ADDR')
            message.save()
            
            success_url = urlresolvers.reverse('contact_sent')
            return HttpResponseRedirect(success_url)
    else:
        form = ContactForm(initial = {
                            'nombre'    : u'Nombre',
                            'email'     : u'Correo Electrónico',
                            'mensaje'   : u'Me gustaría saber más información acerca de...',
                          })
    
    return render_to_response(template_name,
                              { 
				'form': form,
                                'contact_data': contact_data,
                              },
                              context_instance = RequestContext(request))


def contact_form_sent(request, template_name):
    
    try:
        current_site = Site.objects.get_current()
        contact_data = ContactConfig.objects.get()
    except ContactConfig.DoesNotExist:
        contact_data = ''

        
    return render_to_response(template_name,
			      {
				'contact_data': contact_data,
			      },
			      context_instance = RequestContext(request))