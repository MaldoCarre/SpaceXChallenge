from django.core.validators import MaxLengthValidator
from rest_framework import serializers

class CarInfoSerializer(serializers.Serializer):
    type = serializers.CharField(required=True, help_text="Type of card")
    description = serializers.CharField(required=False, help_text="Description")
    title = serializers.CharField(required=False, help_text="Title")
    category = serializers.CharField(required=False, help_text="Category of task")

class ResponseCardSerializer(serializers.Serializer):
    type = serializers.CharField(required=True, help_text="Type of card")
    description = serializers.CharField(required=False, help_text="Description")
    title = serializers.CharField(required=False, help_text="Title")
    category = serializers.CharField(required=False, help_text="Category of task")