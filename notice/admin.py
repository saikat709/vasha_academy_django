from django.contrib import admin

from notice.models import Notice, FAQ, PdfBooks

# Register your models here.
admin.site.register(Notice)
admin.site.register(FAQ)
admin.site.register(PdfBooks)


admin.site.title = "Admin Panel"