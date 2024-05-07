from django.contrib import admin

from statsApp.models import Sotuv


@admin.register(Sotuv)
class SotuvAdmin(admin.ModelAdmin):
    list_display = ('id',)
