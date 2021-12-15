from django.contrib import admin
from .models import *

class ContentAdmin(admin.ModelAdmin):
    list_display=['title','image','addedon']
    search_fields=['title']

admin.site.register(Content,ContentAdmin)
admin.site.register(PatientRegistration)
admin.site.register(messages)
admin.site.register(appointment)
admin.site.register(telepsychiatry)
admin.site.site_header='Restorative Psych'
# Register your models here.
