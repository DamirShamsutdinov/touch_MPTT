from mptt.forms import TreeNodeChoiceField
from rest_framework import viewsets
from rest_framework.response import Response

from departments.models import Department
from departments.serializers import DepartmentSerializer
from staff.models import Specialist, Position
from staff.serializers import SpecialistSerializer, PositionSerializer


class SpecialistViewSet(viewsets.ModelViewSet):
    """Вьюсет для доступа к специалистам"""

    queryset = Specialist.objects.all()
    serializer_class = SpecialistSerializer


class PositionViewSet(viewsets.ModelViewSet):
    """Вьюсет для доступа к позициям штатки"""

    # queryset = Position.objects.all()
    # serializer_class = PositionSerializer

    serializer_class = PositionSerializer
    queryset = Position.objects.all()

    def serialize_tree(self, queryset):
        for obj in queryset:
            data = self.get_serializer(obj).data
            data['children'] = self.serialize_tree(obj.children.all())
            yield data

    def list(self, request):
        queryset = self.get_queryset().filter(level=0)
        data = self.serialize_tree(queryset)
        return Response(data)

    def retrieve(self, request, pk=None):
        self.object = self.get_object()
        data = self.serialize_tree([self.object])
        return Response(data)








class DepartmentViewSet(viewsets.ModelViewSet):
    """Вьюсет для доступа к Департаментам"""

    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
