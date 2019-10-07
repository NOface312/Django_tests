from django.shortcuts import render
from django.http import HttpResponse

def main_page(request):
    context = {
        "title": "main_page",
    }
    return render(request, 'jinja_tests/main_page.html', context)


def contact(request):
    context = {
        "title": "contact",
    }
    return render(request, 'jinja_tests/contact.html', context)


def about(request):
    context = {
        "title": "about",
    }
    return render(request, 'jinja_tests/about.html', context)


def news(request):
    context = {
        "title": "news",
    }
    return render(request, 'jinja_tests/news.html', context)
