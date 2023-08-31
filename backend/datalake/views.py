from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DiagnosisSerializer, PatientDemographicsSerializer, PatientSerializer, PatientSerializerFromNotes, AllPatientDemographicsSerializer, ProviderNoteSerializer, DateSerializer
from .models import Diagnosisview, Demographicsview, Notesview
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
from django.db.models import Count, F, DateTimeField, CharField, Max
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.utils.serializer_helpers import ReturnList
from django.db.models.functions import Cast
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
    serializer_class = ProviderNoteSerializer

    def get_queryset(self):
        return Notesview.objects.filter(patient_id=self.kwargs['pk'])


class ListNoteDates(ListAPIView):
    pagination_class = None
    serializer_class = DateSerializer

    def get_queryset(self):
        return Notesview.objects.filter(patient_id=self.kwargs['pk']).only('date')


class ListSummary(RetrieveAPIView):
    queryset = Demographicsview.objects.all()
    serializer_class = AllPatientDemographicsSerializer

    def get_serializer_context(self):
        return {'date': self.kwargs['date']}

    def get(self, request, *args, **kwargs):
        response = self.retrieve(request, *args, **kwargs)
        clean_response_data(response.data)
        # for k in response.data:
        #     if isinstance(response.data[k], ReturnList):
        #         for v in response.data[k]:
        #             print(type(v))
        #             for (key, value) in v.items():
        #                 if isinstance(value, str):
        #                     v[key] = value.strip()
        return response
