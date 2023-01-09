from rest_framework import serializers

from staff.models import Specialist, Position


class SpecialistSerializer(serializers.ModelSerializer):
    """Сериализатор спецаилиста"""

    class Meta:
        fields = "__all__"
        model = Specialist


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
        fields = ('id', 'name', 'salary', 'description', 'parent', 'children')
