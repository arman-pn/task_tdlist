from rest_framework import serializers
from .models import task

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = task
        fields =['id','title','category','description', 'created_at', 'created_at']
        