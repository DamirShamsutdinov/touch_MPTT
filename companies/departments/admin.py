from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin

from departments.models import Department, Position, Specialist


class SpecialistAdmin(admin.ModelAdmin):
    prepopulated_fields = {"full_name": ("email",)}


admin.site.register(Specialist, SpecialistAdmin)


class PositionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"name": ("salary",)}


admin.site.register(Position, PositionAdmin)


class DepartmentAdmin(DjangoMpttAdmin):
    prepopulated_fields = {"name": ("boss", "staff")}


admin.site.register(Department, DepartmentAdmin)
