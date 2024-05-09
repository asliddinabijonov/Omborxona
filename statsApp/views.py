from django.shortcuts import render
from django.views import View

from .models import *


class SotuvViews(View):
    def get(self, request):
        if request.user.is_authenticated and request.user.is_superuser == False:
            sotuvlar = Sotuv.objects.filter(tarqatuvchi=request.user)
            context = {
                'sotuvlar': sotuvlar
            }
        return render(request, 'statistikalar.html', context)
