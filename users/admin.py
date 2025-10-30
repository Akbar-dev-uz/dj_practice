from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User

# Register your models here.


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'is_staff', 'phone', 'date_joined', 'id']
    list_display_links = ['username', 'phone']

    fieldsets = UserAdmin.fieldsets + (
        ("Qoshimcha maydonlar", {"fields": ("phone",)}),
    )

    add_fieldsets = (
        (None,
         {
             "classes": ("wide",),
             "fields": ("username", "email", "phone", "password1", "password2"),
         },
         ),
    )
