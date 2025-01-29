from rest_framework.viewsets import ModelViewSet

from component.models.component_model import Component
from component.serializers import ComponentSerializer
from rest_framework import status
from rest_framework.response import Response


class ComponentView(ModelViewSet):
    serializer_class = ComponentSerializer
    queryset = Component.objects.all()

    def create(self, request, *args, **kwargs):
        try:
            serialized = self.serializer_class(data=request.data)
            if not serialized.is_valid():
                return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
            created_component = self.serializer_class(
                self.queryset.create(**serialized.data)
            )
            return Response(created_component, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(
                "error creating component", status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
