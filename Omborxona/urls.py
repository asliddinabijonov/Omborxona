from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from mainApp.views import *
from statsApp.views import SotuvViews
from userApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginViews.as_view(), name='login'),
    path('main/', include('mainApp.urls')),
    path('user/', include('userApp.urls')),
    path('stats/', include('statsApp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
