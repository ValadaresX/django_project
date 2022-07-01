from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'global/home.html', context='name': Luiz Otávio)


def contato(request):
    return HttpResponse('contato 1')


def sobre(request):
    return HttpResponse('sobre 1')
