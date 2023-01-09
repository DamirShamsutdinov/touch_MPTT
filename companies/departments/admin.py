from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from departments.models import Department

admin.site.register(Department, MPTTModelAdmin)
# admin.site.register(DepartmentStaff)