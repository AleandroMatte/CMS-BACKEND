from rest_framework.viewsets import ModelViewSet
from post.post_exceptions.post_exceptions import PostException
from post.serializers import PostSerializer
from post.models import Post
from rest_framework.response import Response
from rest_framework import status


class PostViewSet(ModelViewSet):

    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def create(self, request):
        try:
            validated_data = self.serializer_class(data=request.data)
            if not validated_data.is_valid():
                return Response(
                    validated_data.errors, status=status.HTTP_400_BAD_REQUEST
                )
            created_post = self.serializer_class(
                self.queryset.create(**validated_data.data)
            )
            return Response(created_post.data, status=status.HTTP_201_CREATED)
        except PostException as e:
            return Response(e.message, status=e.status)
        except Exception as e:
            return Response("error ocurred while creating post")
