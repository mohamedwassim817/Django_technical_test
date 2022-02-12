from django.contrib import admin
from .models import Formation
from . import models


admin.site.site_header= 'Admin Gazela Technology Academy'
class AutoAdmin(admin.ModelAdmin):
 list_display = ('titre','logo','type','etat')

admin.site.register(models.Formation,AutoAdmin)
