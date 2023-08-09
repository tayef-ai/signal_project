from django.contrib import admin
from .models import Profile
from django.contrib.auth.admin import UserAdmin
from .models import MyUser
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'mobile', 'user_id']


admin.site.register(MyUser, UserAdmin)

