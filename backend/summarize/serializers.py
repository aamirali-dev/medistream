from rest_framework import serializers
from .models import Prompts


class PromptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prompts
        fields = '__all__'
