from rest_framework import serializers
from django.db.models import DateField
from django.db.models.functions import Cast
from .models import Demographicsview, Diagnosisview, Notesview, Vitalsview, Ordersview, Resultsview


class PatientSerializer(serializers.ModelSerializer):
    """
    Serializer for returning initial patient details.

    Properties Included:
        - patient_id
        - patient_first_name
        - last_visit_date
        - gender
        - age_in_years
    """

    class Meta:
        model = Notesview
        fields = [
            'patient_id',
            'patient_first_name',
            'last_visit_date',
            'gender',
            'age_in_years',
        ]

    last_visit_date = serializers.StringRelatedField()
    age_in_years = serializers.IntegerField(default=0)
    gender = serializers.CharField(max_length=1)


# Other serializers have similar docstrings and are used to serialize different data objects.
# I'm including comments for the class names to help differentiate them.
class DiagnosisSerializer(serializers.ModelSerializer):
    """
    Serializer for diagnosis view, simply serializes all the fields
    """

    class Meta:
        model = Diagnosisview
        fields = '__all__'


class ProviderNoteSerializer(serializers.ModelSerializer):
    """
    Serializer for notes from notes view.

    Properties Included:
        - soaptext
        - patient_id
        - note_id
        - created_date_and_time
    """

    class Meta:
        model = Notesview
        exclude = ['soaptext', 'patient_id', 'note_id', 'created_date_and_time']


class VitalSerializer(serializers.ModelSerializer):
    """
    Serializer for Vitals from vitals view.

    Properties Excluded:
        - noteid
        - vitalsid
    """

    class Meta:
        model = Vitalsview
        exclude = ['noteid', 'vitalsid']


class OrderSerializer(serializers.ModelSerializer):
    """
    Serializer for orders from orders view.

    Properties Excluded:
        - patient_id
        - note_id
        - urgency_level

    Include Results for each order based on order id and lab code.
    """

    class Meta:
        model = Ordersview
        exclude = ['patient_id', 'note_id', 'urgency_level']

    results = serializers.SerializerMethodField()

    def get_results(self, instance):
        results_queryset = instance.results.filter(lab_code=instance.lab_code)
        serializer = ResultSerializer(results_queryset, many=True)
        return serializer.data


class ResultSerializer(serializers.ModelSerializer):
    """
    Serialize results from results view
    Properties Excluded: ['patient_id', 'laboratory', 'status', 'latest_result', 'note_id']
    """

    class Meta:
        model = Resultsview
        exclude = ['patient_id', 'laboratory', 'status', 'latest_result', 'note_id']


class AllPatientDemographicsSerializer(serializers.ModelSerializer):
    """
    Serialize All the informations required to send to chatgpt
    It combines information from demographics, diagnosis, notes, orders, and vitals table
    Relevant serializers are used to serialize information for diagnosis, notes, orders, and vitals table
    An overview of properties included are:
        [
            'patientid', 
            'gender', 
            'age_in_years', 
            'marital_status', 
            'date_of_death', 
            'diagnosis', 
            'notes', 
            'orders',
            'vitals',
        ]
    """

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
            'vitals',
        ]

    diagnosis = serializers.SerializerMethodField()
    notes = serializers.SerializerMethodField()
    orders = serializers.SerializerMethodField()
    vitals = serializers.SerializerMethodField()

    def get_diagnosis(self, instance):
        """
        Serialize diagnosis information filtered by date.

        Args:
            instance: The instance of demographics.

        Returns:
            list: List of serialized diagnosis data.
        """
        diagnosis_queryset = self.filter_by_date(instance.diagnosis, 'date_time')
        serializer = DiagnosisSerializer(diagnosis_queryset, many=True)
        return serializer.data

    def get_notes(self, instance):
        """
        Serialize notes information filtered by date.

        Args:
            instance: The instance of demographics.

        Returns:
            list: List of serialized notes data.
        """
        notes_queryset = self.filter_by_date(instance.notes, 'date')
        serializer = ProviderNoteSerializer(notes_queryset, many=True)
        return serializer.data

    def get_orders(self, instance):
        """
        Serialize orders information filtered by date.

        Args:
            instance: The instance of demographics.

        Returns:
            list: List of serialized orders data.
        """
        orders_queryset = self.filter_by_date(instance.orders, 'order_date_time')
        serializer = OrderSerializer(orders_queryset, many=True)
        return serializer.data


    def get_vitals(self, instance):
        """
        Serialize vitals information filtered by date.

        Args:
            instance: The instance of demographics.

        Returns:
            list: List of serialized vitals data.
        """
        vitals_queryset = self.filter_by_date(instance.vitals, 'date_time')
        serializer = VitalSerializer(vitals_queryset, many=True)
        return serializer.data


    def filter_by_date(self, queryset, date_column):
        """
        Simply extracts the date from context (self.context['date']) and filter the queryset with the particular date
        """

        date = self.context.get('date')
        return queryset \
            .annotate(date_compare=Cast(date_column, output_field=DateField())) \
            .filter(date_compare=date)


class DateSerializer(serializers.ModelSerializer):
    """
    Serialize only dates from notes view
    No other information included
    """

    class Meta:
        model = Notesview
        fields = ['date']
