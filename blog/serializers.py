from statistics import mode
from django.forms import fields
from rest_framework import serializers

from .models import Post,Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields='__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields='__all__'


