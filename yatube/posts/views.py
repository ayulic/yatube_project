from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# Главная страница
def index(request):
    return HttpResponse('Ты <i>не можешь</i> получить правильные <b>ответы</b>,<br> '
        'если у тебя нет правильных <s>вопросов</s> запросов.')

def group(request):
    return HttpResponse('Group Posts')


def user(request, name):
    return HttpResponse(f"{str(name).capitalize()}'s Posts")

