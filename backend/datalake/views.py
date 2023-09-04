from datetime import datetime
from django.db.models import Count, F, DateTimeField, Max
from django.db.models.functions import Cast
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import PatientSerializer, AllPatientDemographicsSerializer, DateSerializer
from .models import Demographicsview, Notesview
from .utils import clean_response_data
from .gpt import ChatGPT
from summarize.models import Prompts

import json




class ListPatients(ListAPIView):
    """
    Returns the list of patients, accepts search by patient first name
    Properties Included: patient_id, patient_first_name, last_visit_date, gender, age_in_years
    """

    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['patient_first_name']
    queryset = Notesview.objects.only('patient_id', 'patient_first_name') \
        .order_by('patient_id') \
        .annotate(count=Count('patient_first_name')) \
        .annotate(gender=F('patient_id__gender')) \
        .annotate(age_in_years=F('patient_id__age_in_years')) \
        .annotate(last_visit_date=Max(Cast('date', output_field=DateTimeField())))
    serializer_class = PatientSerializer


class ListNoteDates(ListAPIView):
    """
    Return list of dates for which notes has been taken for the particular patient id
    """

    pagination_class = None
    serializer_class = DateSerializer

    def get_queryset(self):
        return Notesview.objects.filter(patient_id=self.kwargs['pk']).only('date')


class ListSummary(RetrieveAPIView):
    """
    This api performs the following functions
    Step 1: fetch all the data related to a particular patient based on the date selected
    Step 2: send data to chatgpt to generate notes
    Step 3: saves the call in prompts history
    Note: data returned by chatgpt is available in response.data['gpt_response]
    """

    queryset = Demographicsview.objects.all()
    serializer_class = AllPatientDemographicsSerializer

    def get_serializer_context(self):
        self.kwargs['date'] = datetime.strptime(self.kwargs['date'], '%Y-%m-%dT%H:%M:%SZ').date()
        return {'date': self.kwargs['date']}
    
    def get(self, request, *args, **kwargs):
        print(self.request.user.id)
        response = self.retrieve(request, *args, **kwargs)
        clean_response_data(response.data)
        gpt = ChatGPT(json.dumps(response.data))
        response.data['gpt_response'] = gpt.generate_prompt()
        prompt = Prompts.objects.create(user=self.request.user, prompt=response.data['gpt_response'], patient_id=self.kwargs['pk'], date=self.kwargs['date'])
        return response