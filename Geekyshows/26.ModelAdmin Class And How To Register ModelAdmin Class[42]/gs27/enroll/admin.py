from django.contrib import admin
from enroll.models import Student

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    # list_display=('stuid','stuname')
    # list_display=('stuid','stuname','stuemail','stupass')
    # list_display=('id','stuid','stuname','stuemail','stupass')
    # list_display=('id',)
    list_display=['stuid','stuname','stuemail','stupass']

# admin.site.register(Student,StudentAdmin)