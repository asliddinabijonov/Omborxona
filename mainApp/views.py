from django.shortcuts import render
from django.views import View


class BolimViews(View):
    def get(self, request):
        return render(request, 'bo\'limlar.html')

class MijozViews(View):
    def get(self, request):
        return render(request, 'mijozlar.html')

class MahsulotlarViews(View):
    def get(self, request):
        return render(request, 'mahsulotlar.html')
