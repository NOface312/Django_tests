from django.shortcuts import render
from django.http import HttpResponse

def models_tests(request):
    context = {
        "title": "models_tests",
    }
    return render(request, 'models_tests/models.html', context)
