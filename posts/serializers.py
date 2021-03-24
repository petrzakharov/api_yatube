from rest_framework import serializers
from .models import Post, Comment, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('username',)
        model = User


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True
                                          )

    class Meta:
        fields = ('id', 'text', 'author', 'image', 'pub_date')
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True
                                          )

    class Meta:
        fields = ('text', 'created', 'author', 'post')
        model = Comment
