from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomerUser

# Register your models here.


class CustomUserAdmin(UserAdmin):
    # add_form = 
    # form = 
    model = CustomerUser
    list_display = ['username', 'email', 'is_staff']

admin.site.register(CustomerUser, CustomUserAdmin)