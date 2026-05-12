from rest_framework import viewsets, mixins, generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Импорт моделей
from posts.models import Post, Group, Comment, UserProfile

# Импорт сериализаторов
from .serializers import (
    PostSerializer,
    GroupSerializer,
    CommentSerializer,
    UserProfileSerializer
)

# Импорт разрешений
from .permissions import IsAuthorOrReadOnly


# === ВЬЮСЕТЫ ===

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated, IsAuthorOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticated,)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated, IsAuthorOrReadOnly)

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        return Comment.objects.filter(post_id=post_id)

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        post = Post.objects.get(id=post_id)
        serializer.save(author=self.request.user, post=post)




class ProfileView(generics.RetrieveUpdateAPIView):

    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        # Всегда возвращаем профиль текущего пользователя
        profile, _ = UserProfile.objects.get_or_create(user=self.request.user)
        self.check_object_permissions(self.request, profile)
        return profile

    def create(self, request, *args, **kwargs):
        # Профиль создаётся автоматически при регистрации
        return Response(
            {'detail': 'Profile is created automatically upon registration.'},
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )