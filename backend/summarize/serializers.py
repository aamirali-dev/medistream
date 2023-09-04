from rest_framework import serializers
from .models import Prompts


class PromptSerializer(serializers.ModelSerializer):
    """
    Serializer for the Prompts model.

    This serializer is used to serialize `Prompts` model instances, converting them into JSON format.

    Attributes:
        model (Prompts): The model class that this serializer is associated with.
        fields (str or tuple): The fields to be included in the serialized representation.
            In this case, '__all__' is used to include all fields.

    """
    class Meta:
        model = Prompts
        fields = '__all__'
