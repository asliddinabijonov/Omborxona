from django.shortcuts import render
from django.views import View

from .models import *

class SotuvViews(View):
    def get(self, request):
        return render(request, 'statistikalar.html')
