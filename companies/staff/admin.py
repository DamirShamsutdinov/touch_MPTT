from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from mptt.admin import MPTTModelAdmin

from staff.models import Specialist, Position


class SpecialistAdmin(admin.ModelAdmin):
    prepopulated_fields = {"full_name": ("email",)}


admin.site.register(Specialist, SpecialistAdmin)


class PositionAdmin(DjangoMpttAdmin):
    prepopulated_fields = {"name": ("salary",)}


admin.site.register(Position, PositionAdmin)
