# Register your models here.
from django.contrib import admin
from .models import Ticket
from support.models import BestSeller

admin.site.register(Ticket)

@admin.register(BestSeller)
class BestSellerAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)