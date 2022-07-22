from rest_framework import serializers

from .models import Post


class PostsSerializer(serializers.ModelSerializer):

    title = serializers.CharField(required=True, max_length=50)
    content = serializers.CharField(required=True, max_length=255)
    hashtag = serializers.CharField(required=True, max_length=255)

    class Meta:
        model = Post
        fields = ['title', 'writer', 'hashtag', 'content', 'hits', 'likes', 'created_at']
        read_only_fields = ['created_at']
