from statistics import mode
from django.forms import fields
from rest_framework import serializers

from .models import Information

class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Information
        fields='__all__'



