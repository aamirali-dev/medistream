from rest_framework import serializers

from rest_framework import serializers
from .models import Demographicsview, Diagnosisview, Notesview, Vitalsview, Ordersview, Resultsview

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demographicsview
        fields = [
                    'patientid', 
                    'gender', 
                    'age_in_years', 
                    'patient_first_name', 
                    'last_visit_date'
                ]

    patient_first_name = serializers.StringRelatedField()
    last_visit_date = serializers.StringRelatedField()

class PatientSerializerFromNotes(serializers.ModelSerializer):
    class Meta:
        model = Notesview
        fields = [
                    'patient_id', 
                    'patient_first_name', 
                    'last_visit_date',
                    'gender', 
                    'age_in_years',
                    # 'count'
                ]

    last_visit_date = serializers.StringRelatedField()
    age_in_years = serializers.IntegerField(default=0)
    gender = serializers.CharField(max_length=1)
    # count = serializers.IntegerField()

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
        fields = [
            'patientid', 
            'gender', 
            'age_in_years', 
            'marital_status', 
            'date_of_death', 
            'diagnosis', 
            'notes', 
            'orders', 
            'results', 
            'vitals',
        ]


    diagnosis = serializers.SerializerMethodField()
    notes = serializers.SerializerMethodField()
    orders = serializers.SerializerMethodField()
    results = serializers.SerializerMethodField()
    vitals = serializers.SerializerMethodField()

    def get_diagnosis(self, instance):
        date = self.context.get('date')
        diagnosis_queryset = instance.diagnosis.filter(date_time=date)
        serializer = DiagnosisSerializer(diagnosis_queryset, many=True)
        return serializer.data
    
    def get_notes(self, instance):
        date = self.context.get('date')
        notes_queryset = instance.notes.filter(date=date)
        serializer = ProviderNoteSerializer(notes_queryset, many=True)
        return serializer.data
    
    def get_orders(self, instance):
            date = self.context.get('date')
            orders_queryset = instance.orders.filter(order_date_time=date)
            serializer = OrderSerializer(orders_queryset, many=True)
            return serializer.data

    def get_results(self, instance):
        date = self.context.get('date')
        results_queryset = instance.results.filter(result_date_time=date)
        serializer = ResultSerializer(results_queryset, many=True)
        return serializer.data

    def get_vitals(self, instance):
        date = self.context.get('date')
        vitals_queryset = instance.vitals.filter(date_time=date)
        serializer = VitalSerializer(vitals_queryset, many=True)
        return serializer.data


class DateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notesview
        fields = ['date']