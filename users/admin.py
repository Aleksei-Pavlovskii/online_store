from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ("email", "phone", "country", "is_active", "is_staff", "date_joined")
    list_filter = ("is_active", "is_staff", "country", "date_joined")
    search_fields = ("email", "phone", "country")
    ordering = ("email",)
