from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DiagnosisSerializer, PatientDemographicsSerializer, PatientSerializer, AllPatientDemographicsSerializer, ProviderNoteSerializer, DateSerializer
from .models import Diagnosisview, Demographicsview, Notesview
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
from django.db.models import Count, F, DateTimeField, CharField, Max
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from django.db.models.functions import Cast

def get_patients():
    # select patient id, first name, age, 
    query = "SELECT * FROM "

def search():
    pass
# search with first 2 characters
# we can combine both get_patient and search 

def send_details():
    # recieve selected user details, 
    pass 

def send_edited_prompt():
    pass 

def get_history():
    pass 

def get_summary():
    pass 

def get_patient_notes():
    pass 

class ListDiagnosis(ListAPIView):
    queryset = Diagnosisview.objects.all()
    serializer_class = DiagnosisSerializer

class ListPatients(ListAPIView):
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['patient_first_name']
    queryset = Demographicsview.objects \
    .only('patientid', 'gender', 'age_in_years', ) \
    .annotate(patient_first_name=F('diagnosis__patient_first_name')) \
    .annotate(dcount=Count('diagnosis__patient_first_name')) \
    .annotate(last_visit_date=Max(Cast('notes__date', output_field=DateTimeField()))) \
    .order_by('patientid')
    serializer_class = PatientSerializer

class ListNotes(ListAPIView):
    def get_queryset(self):
        return Notesview.objects.filter(patient_id=self.kwargs['pk'])

    serializer_class = ProviderNoteSerializer


class ListNoteDates(ListAPIView):
    pagination_class = None
    def get_queryset(self):
        return Notesview.objects.filter(patient_id=self.kwargs['pk']).only('date')

    serializer_class = DateSerializer

class ListSummary(ListAPIView):
    pid = 4304
    queryset = Demographicsview.objects.select_related('results', 'diagnosis').prefetch_related('notes', 'vitals', 'orders').all()

    serializer_class = AllPatientDemographicsSerializer