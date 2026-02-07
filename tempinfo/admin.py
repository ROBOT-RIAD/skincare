from django.contrib import admin
from .models import TempInfoCollect

# Register your models here.

@admin.register(TempInfoCollect)
class TempInfoCollectAdmin(admin.ModelAdmin):
    list_display = ("id","full_name","email","contact_number","skin_type","birthday","created_at"
)
    search_fields = ("full_name", "email", "contact_number")
    list_filter = ("skin_type","created_at")