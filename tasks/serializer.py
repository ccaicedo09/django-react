from rest_framework import serializers
from .models import Task

class TaskSerialier(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__' # Passes all fields from the model to the serializer
