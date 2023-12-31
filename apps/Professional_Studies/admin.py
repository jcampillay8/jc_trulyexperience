from django.contrib import admin
from .models import Professional_Studies

# Register your models here.
class Professional_Studies_Admin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Professional_Studies, Professional_Studies_Admin)