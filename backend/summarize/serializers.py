from rest_framework import serializers

from rest_framework import serializers
from .models import Demographicsview, Diagnosisview, Notesview, Vitalsview, Ordersview, Resultsview

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demographicsview
        fields = ['patientid', 'gender', 'age_in_years', 'patient_first_name',]

    patient_first_name = serializers.StringRelatedField()

class PatientDemographicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demographicsview
        fields = '__all__'
        

class DiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnosisview
        fields = '__all__'

class ProviderNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notesview
        fields = '__all__'

class VitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vitalsview
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ordersview
        fields = '__all__'

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resultsview
        fields = '__all__'
