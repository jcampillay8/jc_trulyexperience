from django.contrib import admin
from .models import Professional_Training

# Register your models here.
class Professional_Training_Admin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Professional_Training, Professional_Training_Admin)