from django.conf.global_settings import AUTH_USER_MODEL
from django.contrib import admin

from customer.models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "username", "is_superuser", "is_verified", "is_email")
    fields = ("picture", "name", "username", "password", "is_superuser",  "is_verified", "is_email" )
    #form = LoginForm
    #filter_horizontal = ('courses',)



# Register your models here.
# admin.site.register(Profile)
admin.site.register(Customer, CustomerAdmin)