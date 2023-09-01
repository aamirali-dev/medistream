from django.contrib import admin
from django.urls import path
from . import views

###################
# URL Patterns #
###################

urlpatterns = [
    path('prompts/<int:pk>', views.ListPrompts.as_view()),
]