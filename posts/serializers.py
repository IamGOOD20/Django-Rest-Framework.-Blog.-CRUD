from rest_framework import serializers
from .models import Post
from django.contrib.auth import get_user_model

class PostSerializer(serializers.ModelSerializer):
    '''Post model serializer'''
    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'body', 'create_at',)

class UserSerializers(serializers.ModelSerializer):
    '''User model serializer'''
    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)