from rest_framework.viewsets import ModelViewSet

from component.models.component_model import Component
from component.models.component_model_data import ComponentData
from component.serializers import ComponentDataSerializer, ComponentSerializer
from rest_framework import status
from rest_framework.response import Response


class ComponentDataView(ModelViewSet):
    serializer_class = ComponentDataSerializer
    queryset = ComponentData.objects.all()

    def create(self, request, *args, **kwargs):
        try:
            serialized_data = self.serializer_class(data=request.data)
            if not serialized_data.is_valid():
                return Response(
                    serialized_data.errors, status=status.HTTP_400_BAD_REQUEST
                )
            created_component = self.serializer_class(
                self.queryset.create(**serialized_data.data)
            )
            return Response(created_component, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
