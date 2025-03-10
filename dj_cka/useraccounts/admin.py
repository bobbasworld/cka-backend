from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.admin import UserAdmin
from useraccounts.models import MyUser


class MyUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined',
                    'last_login', 'is_admin', 'is_staff',)
    search_fields = ('email', 'username',)
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(MyUser, MyUserAdmin)
