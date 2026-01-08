from django.contrib import admin
from .models import Punejob,BangJob,BiharJob
# Register your models here.

class PuneJobAdmin(admin.ModelAdmin):
    list_display=["id","date","company","title","address","salary","email","phone"]
    
admin.site.register(Punejob,PuneJobAdmin)

class BangAdmin(admin.ModelAdmin):
    list_display=["id","date","company","title","address","salary","email","phone"]
admin.site.register(BangJob,BangAdmin)

class BiharAdmin(admin.ModelAdmin):
    list_display=["id","date","company","title","address","salary","email","phone"]
admin.site.register(BiharJob,BiharAdmin)