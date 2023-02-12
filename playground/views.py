from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def say_hallo(request):
    x = 1
    y = 1
    return render(request, 'hello.html', {'name': 'Achilles'})
