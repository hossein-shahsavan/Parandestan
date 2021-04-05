from django.contrib import admin
from .models import User, PhoneOTP
from django.contrib.auth.models import Group


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('phone', 'full_name', 'email', 'is_admin', 'is_active')
    list_filter = ('is_admin', 'is_active')
    search_fields = ('phone', 'full_name')


admin.site.register(PhoneOTP)
admin.site.unregister(Group)
