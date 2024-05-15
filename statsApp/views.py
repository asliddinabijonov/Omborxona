from django.shortcuts import render, redirect
from django.views import View
from datetime import datetime

from .models import *


class SotuvViews(View):
    def get(self, request):
        if request.user.is_authenticated:
            sotuvlar = Sotuv.objects.filter(tarqatuvchi=request.user)
            mijozlar = Mijoz.objects.filter(tarqatuvchi=request.user)
            mahsulotlar = Mahsulot.objects.filter(tarqatuvchi=request.user)
            summa = sum(sotuvlar.values_list('summa', flat=True))
            qarz = sum(sotuvlar.values_list('qarz', flat=True))
            context = {
                'sotuvlar': sotuvlar,
                'mijozlar': mijozlar,
                'mahsulotlar': mahsulotlar,
                'statistika': {
                    'summa': summa,
                    'qarz': qarz
                }
            }
            return render(request, 'statistikalar.html', context)
        return redirect('login')

    def post(self, request):
        if request.user.is_authenticated:
            summa = float(request.POST.get('summa', 0))
            mahsulot = Mahsulot.objects.get(id=request.POST.get('mahsulot'))
            mijoz = Mijoz.objects.get(id=request.POST.get('mijoz'))
            miqdor = float(request.POST.get('miqdor', 0))
            if summa == 0:
                summa = float(mahsulot.narx2) * miqdor
            tolandi = float(request.POST.get('tolandi', 0))
            qarz = float(request.POST.get('qarz', 0))
            if tolandi == 0 and qarz == 0:
                qarz = summa
            elif tolandi == 0 and qarz != 0:
                if summa < qarz:
                    return redirect('statistika')
                tolandi = summa - qarz
            elif tolandi != 0 and qarz == 0:
                if summa < tolandi:
                    return redirect('statistika')
                qarz = summa - tolandi
            sana = request.POST.get('sana')
            if sana == '2000-01-01':
                sana = datetime.now().strftime('%Y-%m-%d')
            if miqdor > mahsulot.miqdor:
                return redirect('statistika')
            sotuv = Sotuv.objects.create(
                tarqatuvchi=request.user,
                mahsulot=mahsulot,
                mijoz=mijoz,
                miqdor=miqdor,
                summa=summa,
                tolandi=tolandi,
                qarz=qarz,
                sana=sana,
            )
            mahsulot.miqdor -= miqdor
            mahsulot.save()
            mijoz.qarz = sum(Sotuv.objects.filter(tarqatuvchi=request.user, mijoz=mijoz).values_list("qarz", flat=True))
            mijoz.save()
            return redirect('statistika')
        return redirect('login')


class UpdateViews(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            sotuv = Sotuv.objects.get(tarqatuvchi=request.user, id=pk)
            mahsulot = Mahsulot.objects.get(id=sotuv.mahsulot.id, tarqatuvchi=request.user)
            mijoz = Mijoz.objects.get(id=sotuv.mijoz.id, tarqatuvchi=request.user)
            context = {
                'sotuv': sotuv,
                'mahsulot': mahsulot,
                'mijoz': mijoz,
            }
            return render(request, 'statistika-tahrirlash.html', context)
        return redirect('login')

    def post(self, request, pk):
        if request.user.is_authenticated:
            sotuv = Sotuv.objects.filter(id=pk, tarqatuvchi=request.user)
            miqdor = float(request.POST.get('miqdor'))
            mahsulot = sotuv.first().mahsulot

            if mahsulot.miqdor >= (miqdor - float(sotuv.first().miqdor)):
                mahsulot.miqdor += float(sotuv.first().miqdor) - miqdor
                mahsulot.save()

            tolandi = request.POST.get('tolandi')
            summa = request.POST.get('summa')
            if sotuv.first().miqdor != miqdor:
                summa = float(sotuv.first().mahsulot.narx2) * miqdor
            qarz = float(summa) - float(tolandi)
            sotuv.update(
                tarqatuvchi=request.user,
                miqdor=miqdor,
                summa=summa,
                tolandi=tolandi,
                qarz=qarz,
            )
            return redirect('statistika')
        return redirect('login')


class DeleteSotuvView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            sotuv = Sotuv.objects.get(id=pk)
            if sotuv.tarqatuvchi == request.user:
                sotuv.delete()
            return redirect('statistika')
        return redirect('login')
