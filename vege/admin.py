from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Receipe)

admin.site.register(StudentID)
admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Subject)
class SubjectsMarksAdmin(admin.ModelAdmin):
    list_display = ["student","subject","marks"]
admin.site.register(SubjectsMarks,SubjectsMarksAdmin)