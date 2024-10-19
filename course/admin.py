from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Course, Exam, Result

# Register your models here.


class ExamAdmin(ModelAdmin):
    filter_horizontal = ('questions',)

class CourseAdmin(ModelAdmin):
    filter_horizontal = ('exams',) #  "enrollments")


admin.site.register(Course, CourseAdmin)
admin.site.register(Exam, ExamAdmin)
admin.site.register(Result)