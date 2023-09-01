from typing import Any
from django.db.models.query import QuerySet
from rest_framework.generics import ListAPIView
from .serializers import PromptSerializer
from .models import Prompts

class ListPrompts(ListAPIView):
    serializer_class = PromptSerializer

    def get_queryset(self):
        return Prompts.objects.filter(user_id=self.kwargs['pk'])

