from django.contrib import admin
from .models import Employee
# Register your models here.


class EmployeeSAdmin(admin.ModelAdmin):
    list_display=['eid','name','salary','mail','city',]
admin.site.register(Employee,EmployeeSAdmin)
