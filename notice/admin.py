from django.contrib import admin

from notice.models import Notice, FAQ, PdfBooks, WebsiteConfig


# Register your models here.
admin.site.register(WebsiteConfig)
admin.site.register(Notice)
admin.site.register(FAQ)
admin.site.register(PdfBooks)
