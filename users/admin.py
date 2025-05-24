from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'phone', 'gender', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('phone', 'birth_year', 'birth_month', 'birth_day', 'gender', 'address', 'point')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('email', 'phone', 'birth_year', 'birth_month', 'birth_day', 'gender', 'address')}),
    )