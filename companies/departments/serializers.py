from rest_framework import serializers

from departments.models import Department, Position, Specialist


class SpecialistSerializer(serializers.ModelSerializer):
    """Сериализатор спецаилиста"""

    class Meta:
        model = Specialist
        fields = "__all__"


class StaffSerializer(serializers.ModelSerializer):
    """Сериализатор спецаилиста"""
    position = serializers.ReadOnlyField(source="position.name")

    class Meta:
        model = Specialist
        fields = ('full_name', 'position', 'email',)


class PositionSerializer(serializers.ModelSerializer):
    """Сериализатор модели Позиция"""

    class Meta:
        model = Position
        fields = "__all__"


class DepartmentSerializer(serializers.ModelSerializer):
    """Сериализатор модели отношения Младшее Подразделение"""

    # boss = serializers.ReadOnlyField(source="boss.full_name")
    boss = StaffSerializer()
    staff = StaffSerializer(many=True)

    class Meta:
        model = Department
        fields = (
            'id',
            'name',
            'description',
            'boss',
            'staff',
            'parent',
            'children'
        )
