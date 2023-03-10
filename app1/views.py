from django.http import HttpResponse
from django.shortcuts import render
from django.utils.translation import gettext as _
from django.views import View


class HomeView(View):
    def get(self, request):
        string = _('Hello world')
        context = {'string': string}

        return HttpResponse(render(request, 'home.html', context))


