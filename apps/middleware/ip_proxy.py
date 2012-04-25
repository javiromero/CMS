from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import RequestContext, Template, loader

class SetRemoteAddrFromForwardedFor(object) :
    def process_request(self, request) :
        try :
            real_ip = request.META['HTTP_X_FORWARDED_FOR']
        except KeyError :
            return None
        else :
            real_ip = real_ip.split(",")[0].strip()
            request.META['REMOTE_ADDR'] = real_ip