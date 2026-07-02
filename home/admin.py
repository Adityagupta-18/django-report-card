from django.contrib import admin
from home.models import *
# Register your models here.
admin.site.register(Department)
admin.site.register(StudentID)

class StudentAdmin(admin.ModelAdmin):
    list_display=['student_name','department','student_id']

admin.site.register(Student,StudentAdmin)

admin.site.register(Subject)

class SubjectmarksAdmin(admin.ModelAdmin):
    list_display=['student','subject','marks']
admin.site.register(subjectmarks,SubjectmarksAdmin)