from rest_framework.serializers import ModelSerializer

from component.models.component_model import Component
from component.models.component_model_data import ComponentData


class ComponentSerializer(ModelSerializer):
    class Meta:
        model = Component
        fields = "__all__"


class ComponentDataSerializer(ModelSerializer):
    class Meta:
        model = ComponentData
        fields = "__all__"
