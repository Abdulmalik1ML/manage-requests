from django.contrib import admin
from .models import Service, ServiceRequest
# Register your models here.
admin.site.register(Service)
class serviseAdmin(admin.ModelAdmin):
    list_display = ("id", 'title')