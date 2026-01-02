from django.contrib import admin
from .models import User,Profile,PasswordReserOTP
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.


#admin
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ["id","email" ,"role"]
    search_fields =["email","role"]
    list_filter =["role"]

    fieldsets = BaseUserAdmin.fieldsets + (
        ("Custom Fields", {"fields": ("role",)}),
    )

    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ("Custom Fields", {"fields": ("role",)}),
    )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=["id","user","full_name","gender","image","created_at","updated_at"]
    search_fields = ["full_name", "phone", "user__email"]
    list_filter = ["full_name","gender"]



@admin.register(PasswordReserOTP)
class PasswordResetOTPAdmin(admin.ModelAdmin):
    list_display = ('user', 'otp', 'created_at', 'is_verified')
    search_fields = ('user__email', 'otp')
    list_filter = ('is_verified',)
    ordering = ('created_at',)


