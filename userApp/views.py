from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View

from .models import *


class LoginViews(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        tarqatuvchi = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if tarqatuvchi is not None:
            login(request, tarqatuvchi)
            return redirect('bolimlar')
        return redirect('login')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
