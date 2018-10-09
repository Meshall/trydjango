from django.contrib import admin

# Register your models here.
from .models import UserInfo



class UserInfoAdmin(admin.ModelAdmin):

    fields = (
        'user_name',
        'user_ip',
        'user_password',
        'user_agent',
        'cookies',
    )

    list_display = (
        'user_name',
        'user_password',
        'user_ip',
        'user_agent',
    )

admin.site.register(UserInfo, UserInfoAdmin)
