from django.shortcuts import render, redirect
from django.views import View
from .models import *


class BolimlarViews(View):
    def get(self, request):
        return render(request, 'bo\'limlar.html')


class MijozViews(View):
    def get(self, request):
        if request.user.is_authenticated and request.user.is_superuser == False:
            mijozlar = Mijoz.objects.filter(tarqatuvchi=request.user)
            context = {
                'mijozlar': mijozlar
            }
            return render(request, 'mijozlar.html', context)
        return redirect('login')




class MahsulotlarViews(View):
    def get(self, request):
        if request.user.is_authenticated and request.user.is_superuser == False:
            mahsulotlar = Mahsulot.objects.filter(tarqatuvchi=request.user)
            context = {
                'mahsulotlar': mahsulotlar
            }
            return render(request, 'mahsulotlar.html', context)
        return redirect('login')

class DeleteMahsulotlarView(View):
    def get(self, request, pk):
        if request.user.is_authenticated and request.user.is_superuser == False:
            mijozlar = Mahsulot.objects.get(id=pk)
            mijozlar.delete()
            return redirect('mahsulotlar')
        return redirect('login')