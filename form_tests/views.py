from django.shortcuts import render
from django.http import HttpResponse

def form_tests(request):
    context = {
        "title": "form_tests",
    }

    return render(request, 'form_tests/form.html', context)


def search(request):
    if request.method == "GET":
        if 'q' in request.GET:
            return HttpResponse("Вы хотели найти строку %s" % request.GET['q'])
        else:
            return HttpResponse("Вы отправили пустую форму")
    context = {
        "title": "form_tests",
    }

    return render(request, 'form_tests/form.html', context)


def file_input(request):
    context = {
        "title": "form_tests",
    }

    return render(request, 'form_tests/form.html', context)
