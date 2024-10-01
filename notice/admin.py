from django.contrib import admin

from notice.models import Notice, FAQ

# Register your models here.
admin.site.register(Notice)
admin.site.register(FAQ)


admin.site.title = "Admin Panel"