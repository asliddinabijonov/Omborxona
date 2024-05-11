import datetime

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

    def post(self, request):
        if request.user.is_authenticated:
            Mijoz.objects.create(
                tarqatuvchi=request.user,
                ism=request.POST.get('ism', None),
                dokon=request.POST.get('dokon', None),
                tel=request.POST.get('tel', None),
                manzil=request.POST.get('manzil', None),
                oluvchi=request.POST.get('oluvchi', None),
            )
            return redirect('mijozlar')
        return redirect('login')


class DeleteMijozlarView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            mijoz = Mijoz.objects.get(id=pk)
            if mijoz.tarqatuvchi == request.user:
                mijoz.delete()
            return redirect('mijozlar')
        return redirect('login')


class UpdateMijozlarViews(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            mijoz = Mijoz.objects.get(id=pk)
            context = {
                'mijoz': mijoz
            }
            return render(request, 'mijoz-tahrirlash.html', context)
        return redirect('mijozlar')

    def post(self, request, pk):
        if request.user.is_authenticated:
            if Mijoz.objects.get(id=pk).tarqatuvchi == request.user:
                Mijoz.objects.filter(id=pk).update(
                    tarqatuvchi=request.user,
                    ism=request.POST.get('ism', None),
                    dokon=request.POST.get('dokon', None),
                    tel=request.POST.get('tel', None),
                    manzil=request.POST.get('manzil', None),
                    oluvchi=request.POST.get('oluvchi', None),
                )
            return redirect('mijozlar')
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

    def post(self, request):
        if request.user.is_authenticated:
            Mahsulot.objects.create(
                tarqatuvchi=request.user,
                nom=request.POST.get("nom", None),
                brand=request.POST.get("brand", None),
                narx1=request.POST.get("narx1", None),
                narx2=request.POST.get("narx2", None),
                miqdor=request.POST.get("miqdor", None),
                olchov=request.POST.get("olchov", None),
                sana=request.POST.get("sana", None),
            )
            return redirect('mahsulotlar')
        return redirect('login')


class DeleteMahsulotlarView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            mahsulot = Mahsulot.objects.get(id=pk)
            if mahsulot.tarqatuvchi == request.user:
                mahsulot.delete()
            return redirect('mahsulotlar')
        return redirect('login')


class UpdateMahsulotlarView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            mahsulot = Mahsulot.objects.get(id=pk)
            context = {
                'mahsulot': mahsulot
            }
            return render(request, 'mahsulot-tahrirlash.html', context)
        return redirect('mahsulotlar')

    def post(self, request, pk):
        if request.user.is_authenticated:
            if Mahsulot.objects.get(id=pk).tarqatuvchi == request.user:
                Mahsulot.objects.filter(id=pk).update(
                    tarqatuvchi=request.user,
                    nom=request.POST.get("nom", None),
                    brand=request.POST.get("brand", None),
                    narx1=request.POST.get("narx1", None),
                    narx2=request.POST.get("narx2", None),
                    miqdor=request.POST.get("miqdor", None),
                    olchov=request.POST.get("olchov", None),
                    sana=datetime.datetime.now().strftime("%Y-%m-%d")
                )
            return redirect('mahsulotlar')
        return redirect('login')
