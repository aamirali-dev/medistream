from rest_framework import serializers

from rest_framework import serializers
from .models import Demographicsview, Diagnosisview, Notesview, Vitalsview, Ordersview, Resultsview

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demographicsview
        fields = ['patientid', 'gender', 'age_in_years', 'patient_first_name', 'last_visit_date']

    patient_first_name = serializers.StringRelatedField()
    last_visit_date = serializers.StringRelatedField()

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


class AllPatientDemographicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demographicsview
        fields = '__all__'
    diagnosis = DiagnosisSerializer(many=True)
    notes = ProviderNoteSerializer(many=True)
    orders = OrderSerializer(many=True)
    results = ResultSerializer(many=True)
    vitals = VitalSerializer(many=True)

class DateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notesview
        fields = ['date']