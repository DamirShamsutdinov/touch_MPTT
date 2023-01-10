from departments.models import Department, Specialist, Position
from rest_framework import serializers


class SpecialistSerializer(serializers.ModelSerializer):
    """Сериализатор спецаилиста"""

    class Meta:
        model = Specialist
        fields = "__all__"


class StaffSerializer(serializers.ModelSerializer):
    """Сериализатор спецаилиста"""

    class Meta:
        model = Specialist
        fields = ('full_name', 'email',)


# class PositionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Position
#         fields = ('id', 'name', 'salary', 'description', 'parent', 'children')
#
#     def get_fields(self):
#         fields = super(PositionSerializer, self).get_fields()
#         fields['children'] = PositionSerializer(many=True)
#         return fields


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
