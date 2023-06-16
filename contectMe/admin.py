from django.contrib import admin
from .models import ContectMe

# Register your models here.
class ContactMeAdmin(admin.ModelAdmin):
    list_display =["name"]
admin.site.register(ContectMe,ContactMeAdmin)