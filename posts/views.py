from .serializers import PostSerializer, CommentSerializer, UserSerializer
from .models import Post, User, Comment
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly

from django.shortcuts import get_object_or_404
from rest_framework import viewsets


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly
    )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        # serializer.save(
        #     author=self.request.user,
        #     professor_id=self.kwargs.get('pk'),
        # )


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly
    )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments
        # queryset = super(ProfessorReviewList, self).get_queryset()
        # return queryset.filter(professor__pk=self.kwargs.get('pk'))




class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
