from django.shortcuts import render
from django.http import HttpResponse

def req_tests(request):
    context = {
        "title": "reg_tests",
    }
    return render(request, 'reg_tests/test.html', context)
