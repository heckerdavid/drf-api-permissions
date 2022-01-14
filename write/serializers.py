from rest_framework import serializers
from .models import Write

class WriteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'author', 'title','review', 'created_at')
        model = Write