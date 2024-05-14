from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from mainApp import admin
from .views import *

urlpatterns = [
                  path('statistika/', SotuvViews.as_view(), name='statistika'),
                  path('statistika/<int:pk>/delete/', DeleteSotuvView.as_view(), name='sotuvdetele'),
                  path('statistika/<int:pk>/update/', UpdateViews.as_view(), name='sotuvupdate'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
