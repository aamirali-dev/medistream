from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('diagnosis/', views.ListDiagnosis.as_view()),
    path('patients/', views.ListPatients.as_view()),
    # path('summary/<int:pk>', views.ListSummary.as_view()),
    path('summary/<int:pk>', views.ListSummary.as_view()),
    path('notes/<int:pk>', views.ListNotes.as_view()),
    path('dates/<int:pk>', views.ListNoteDates.as_view()),
]