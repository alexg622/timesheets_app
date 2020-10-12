from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
test = 'true'
# use {%%} for code blocks
#  {{}} to print code in html
from .models import User

def home(request):
    context = {
        'data': test
    }
    return render(request, 'users/info.html', context)
