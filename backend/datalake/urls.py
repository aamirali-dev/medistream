from django.contrib import admin
from django.urls import path
from . import views

"""
# URL Patterns #
"""

urlpatterns = [
    path('patients/', views.ListPatients.as_view()),
    path('summary/<int:pk>/<str:date>', views.ListSummary.as_view()),
    path('dates/<int:pk>', views.ListNoteDates.as_view()),
]