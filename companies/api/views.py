from mptt.forms import TreeNodeChoiceField
from rest_framework import viewsets
from departments.models import Department
from departments.serializers import DepartmentSerializer, PositionSerializer
from staff.models import Specialist, Position
from staff.serializers import SpecialistSerializer


class SpecialistViewSet(viewsets.ModelViewSet):
    """Вьюсет для доступа к специалистам"""

    queryset = Specialist.objects.all()
    serializer_class = SpecialistSerializer


class PositionViewSet(viewsets.ModelViewSet):
    """Вьюсет для доступа к позициям штатки"""

    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    """Вьюсет для доступа к Департаментам"""

    queryset = TreeNodeChoiceField(Department.objects.all())
    serializer_class = DepartmentSerializer
