from django.shortcuts import render
from django.views import View

from .models import *


class LoginViews(View):
    def get(self, request):
        return render(request, 'login.html')
