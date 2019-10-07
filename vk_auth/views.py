from django.shortcuts import render
from django.http import HttpResponse

def vk_auth(request):
    context = {
        "title": "vk_auth",
    }
    return render(request, 'vk_auth/index.html', context)
