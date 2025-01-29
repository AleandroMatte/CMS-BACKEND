from rest_framework.routers import DefaultRouter
from post.views.PostView import PostViewSet

router = DefaultRouter()
router.register(r"", PostViewSet, basename="post")
urlpatterns = [*router.urls]
