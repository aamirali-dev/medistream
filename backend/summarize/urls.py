from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('diagnosis/', views.ListDiagnosis.as_view()),
    path('patients/', views.ListPatients.as_view()),

]