from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    '''Post model serializer'''
    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'body', 'create_at']
