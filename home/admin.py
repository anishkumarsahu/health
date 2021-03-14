from django.contrib import admin

# Register your models here.
from home.models import AdminUser


@admin.register(AdminUser)
class AdminUserAdmin(admin.ModelAdmin):
    list_display = ("name", "phoneNumber","email", "password", "userType","isDeleted",)
    search_fields = ["name", "phoneNumber","email", "password", "userType", ]
