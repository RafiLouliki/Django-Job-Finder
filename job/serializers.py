from statistics import mode
from django.forms import fields
from rest_framework import serializers

from .models import Job,Category,apply

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model=Job
        fields='__all__'


class ApplySerializer(serializers.ModelSerializer):
    class Meta:
        model=apply
        fields='__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'
