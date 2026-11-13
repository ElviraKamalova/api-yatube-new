from rest_framework import serializers

from posts.models import Comment, Group, Post


class AuthorModelSerializer(serializers.ModelSerializer):
    """Базовый сериализатор для моделей с полем автора."""

    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор для модели сообщества (Group)."""

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class PostSerializer(AuthorModelSerializer):
    """Сериализатор для модели публикации (Post)."""

    class Meta:
        model = Post
        fields = (
            'id',
            'text',
            'pub_date',
            'author',
            'image',
            'group'
        )


class CommentSerializer(AuthorModelSerializer):
    """Сериализатор для модели комментария (Comment)."""

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('post',)
