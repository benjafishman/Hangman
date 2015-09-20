from django.shortcuts import render

# Create your views here.

__author__ = 'benfishman'

from django.shortcuts import render
from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'sefaria_daily_dose/index.html')
