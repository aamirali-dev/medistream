from datetime import datetime
from django.db.models import Count, F, DateTimeField, CharField, Max
from django.db.models.functions import Cast
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import DiagnosisSerializer, PatientSerializer, \
    PatientSerializerFromNotes, AllPatientDemographicsSerializer, ProviderNoteSerializer, DateSerializer
from .models import Diagnosisview, Demographicsview, Notesview
from .utils import clean_response_data


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

#########################################################
# Get all unique Patient IDs from Provider Notes Table #
#########################################################

class ListPatientsFromNotes(ListAPIView):
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['patient_first_name']
    queryset = Notesview.objects.only('patient_id', 'patient_first_name') \
        .order_by('patient_id') \
        .annotate(count=Count('patient_first_name')) \
        .annotate(gender=F('patient_id__gender')) \
        .annotate(age_in_years=F('patient_id__age_in_years')) \
        .annotate(last_visit_date=Max(Cast('date', output_field=DateTimeField())))
    serializer_class = PatientSerializerFromNotes


class ListNotes(ListAPIView):
    def get_queryset(self):
        return Notesview.objects.filter(patient_id=self.kwargs['pk'])

    serializer_class = ProviderNoteSerializer


class ListNoteDates(ListAPIView):
    pagination_class = None

    def get_queryset(self):
        return Notesview.objects.filter(patient_id=self.kwargs['pk']).only('date')

    serializer_class = DateSerializer


class ListSummary(RetrieveAPIView):
    queryset = Demographicsview.objects.all()

    def get_serializer_context(self):
        date = self.kwargs['date']
        date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ').date()
        return {'date': date}
    
    def get(self, request, *args, **kwargs):
        response = self.retrieve(request, *args, **kwargs)
        clean_response_data(response.data)

        return response
        

    serializer_class = AllPatientDemographicsSerializer
