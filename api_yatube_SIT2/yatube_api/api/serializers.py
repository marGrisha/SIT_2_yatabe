from rest_framework import serializers
from posts.models import Post, Group, Comment, UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('avatar', 'bio', 'city', 'birth_date', 'hobbies', 'education', 'website')

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    author_profile = UserProfileSerializer(source='author.profile', read_only=True)
    # Явное поле для возврата абсолютного URL картинки
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Post
        fields = ('id', 'text', 'pub_date', 'author', 'author_profile', 'image', 'group')

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('post', 'author')