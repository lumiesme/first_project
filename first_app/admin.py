from django.contrib import admin
from .models import Student, StudentAdmin, Teacher, TeachersAdmin
# Register your models here.
# Show admin page
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher,TeachersAdmin)



