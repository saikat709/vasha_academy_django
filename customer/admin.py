from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import LoginForm
from .models import Profile, Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ("fullname", "number", "is_verified")
    fields = ("fullname", "number", "password", "is_verified" )
    #form = LoginForm
    # filter_horizontal = ('courses',)



# Register your models here.
# admin.site.register(Profile)
admin.site.register(Customer, CustomerAdmin)