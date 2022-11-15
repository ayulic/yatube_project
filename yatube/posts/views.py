from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# Импортируем загрузчик.
from django.template import loader


# Главная страница
def index(request):
    template = 'posts/index.html'
    # return HttpResponse(f'Main page (index.html)')
    return render(request, template)

    return render(request, template)

def group(request):
    template = 'posts/group_list.html'
    return render(request, template)


def user(request, name):
    return HttpResponse(f"{str(name).capitalize()}'s Posts")

