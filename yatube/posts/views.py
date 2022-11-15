from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# Импортируем загрузчик.
from django.template import loader


# Главная страница
def index(request):
    # template's url
    template = 'posts/index.html'
    # page title
    title = "Yatube: Main Page"
    text = 'Yatube Main Page'
    # data dictionary
    context = {
        'title': title,
        'text': text
    }
    # return HttpResponse(f'Main page (index.html)')
    return render(request, template, context)

    return render(request, template)

def group(request):
    template = 'posts/group_list.html'
    # page title
    title = "Yatube: Groups List"
    text = 'Yatube Groups Info'
    # data dictionary
    context = {
        'title': title,
        'text':text
    }

    return render(request, template, context)


def user(request, name):
    return HttpResponse(f"{str(name).capitalize()}'s Posts")

