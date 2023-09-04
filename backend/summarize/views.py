from typing import Any
from django.db.models.query import QuerySet
from rest_framework.generics import ListAPIView
from .serializers import PromptSerializer
from .models import Prompts


class ListPrompts(ListAPIView):
    """
    API view for listing prompts issued by a specific user.

    This view retrieves a list of prompts issued by a user based on the user's primary key (`pk`) in the URL.
    It uses the `PromptSerializer` to serialize the data.

    Attributes:
        serializer_class (PromptSerializer): The serializer class for serializing prompts.

    Methods:
        get_queryset(self): Retrieves the queryset of prompts for the specified user.

    """
    serializer_class = PromptSerializer

    def get_queryset(self):
        """
        Get a queryset of prompts issued by a specific user.

        Returns:
            QuerySet: A queryset of prompts issued by the user identified by 'pk' in the URL.

        """
        # Filter prompts based on the user's ID from the URL
        return Prompts.objects.filter(user_id=self.kwargs['pk'])
