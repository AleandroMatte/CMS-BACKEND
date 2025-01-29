from rest_framework.routers import DefaultRouter

from component.views.component_view import ComponentView

component_view_router = DefaultRouter()
component_view_router.register("", ComponentView, basename="components")

urlpatterns = [
    *component_view_router.urls,
]
