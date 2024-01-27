from django.contrib import admin
from .models import Fintech_Funding, Category
# Register your models here.


class FintechFundingAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'currency',
                    'date', 'category', 'owner',)
    search_fields = ('name', 'amount', 'currency',
                     'date', 'category', 'owner',)
    list_per_page = 25


admin.site.register(Category)
admin.site.register(Fintech_Funding, FintechFundingAdmin)