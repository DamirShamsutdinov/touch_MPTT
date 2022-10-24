from rest_framework import viewsets

from companies.departments.models import CurrentDepartment
from companies.departments.serializers import CurrentDepartmentSerializer
from companies.staff.models import Boss, CurrentSpecialist
from companies.staff.serializers import BossSerializer, \
    CurrentSpecialistSerializer


class CurrentSpecialistViewSet(viewsets.ModelViewSet):
    """Вьюсет для доступа к штату Боссов>"""

    queryset = CurrentSpecialist.objects.all()
    serializer_class = CurrentSpecialistSerializer


class CurrentDepartmentViewSet(viewsets.ModelViewSet):
    """Вьюсет для доступа к Департаментам"""

    queryset = CurrentDepartment.objects.all()
    serializer_class = CurrentDepartmentSerializer