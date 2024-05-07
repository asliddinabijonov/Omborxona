from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from mainApp.views import *
from statsApp.views import SotuvViews
from userApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginViews.as_view(), name='login'),
    path('bolim/', BolimViews.as_view(), name='bolim'),
    path('mijozlar/', MijozViews.as_view(), name='mijozlar'),
    path('mahsulotlar/', MahsulotlarViews.as_view(), name='mahsulotlar'),
    path('statistika/', SotuvViews.as_view(), name='statistika'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
