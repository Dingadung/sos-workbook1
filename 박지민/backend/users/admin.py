from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'user_id',
        'hobby',
    )
    search_fields = ('user_id', 'hobby')


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)  # Admin페이지의 GROUP삭제
