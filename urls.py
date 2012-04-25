from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.simple import direct_to_template, redirect_to, HttpResponse

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    (r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /admin\nDisallow: /static\nDisallow: /media", mimetype="text/plain")),
    url(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to',{'url': '/media/img/favicon.ico'}),
    
    url(r'^c/', include('catalog.urls')),
    url(r'^contacto/', include('contact.urls')),
    url(r'^quienes/', include('quienes.urls')),
    url(r'^newsletter/', include('newsletter.urls')), 
)

handler404 = 'web.views.error_404'
# En los errores 500 se debe devolver html plano,
# para que no puedan darse errores del servidor adicionales
# handler500 = 'web.views.error_500' 

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    )
    # Easy way to check error templates on development
    urlpatterns += patterns('',
        #(r'^404/$', 'web.views.error_404'),
        (r'^404/$', direct_to_template, {'template': '404.html'} ),
        (r'^500/$', direct_to_template, {'template': '500.html'} ),
        (r'^503/$', direct_to_template, {'template': '503.html'} ),
    )

urlpatterns += patterns('',
    url(r'^', include('web.urls')),
)