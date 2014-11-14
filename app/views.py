from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic import View


class AppView(View):
    """"""

    def get(self, request):
        """"""""
        return render_to_response('main.html', context_instance=RequestContext(request))
