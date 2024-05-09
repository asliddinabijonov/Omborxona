from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from mainApp import admin
from .views import *

urlpatterns = [
    path('bolimlar/', BolimlarViews.as_view(), name='bolimlar'),
    path('mahsulotlar/', MahsulotlarViews.as_view(), name='mahsulotlar'),
    path('mijozlar/', MijozViews.as_view(), name="mijozlar"),
    path('mahsulotlar/<int:pk>/delete', DeleteMahsulotlarView.as_view(), name='deletemahsulotlar'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
