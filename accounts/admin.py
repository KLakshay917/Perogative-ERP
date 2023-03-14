from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class use(UserAdmin):
    list_display = ['username','email', 'user_type']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal Info'), {'fields': ('email',)}),
        (('Permissions'), {'fields': ('user_type',)}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
admin.site.register(CustomUser,use)
admin.site.register(StudentEnquiry)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Admin)
admin.site.register(Teacher)
admin.site.register(Caller)
admin.site.register(Attendance)

