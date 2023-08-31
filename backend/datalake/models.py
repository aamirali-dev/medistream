# connecting sql server
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

_LAKE_APP_LABEL = 'datalake'

class Demographicsview(models.Model):
    patientid = models.IntegerField(db_column='PatientID', primary_key=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=1, blank=True, null=True)  # Field name made lowercase.
    date_of_birth = models.DateTimeField(db_column='Date of Birth', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    age_in_years = models.IntegerField(db_column='Age In Years', null=True, blank=True, default=0)
    marital_status = models.CharField(db_column='Marital Status', max_length=9)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    race = models.TextField(db_column='Race', blank=True, null=True)  # Field name made lowercase.
    race_category = models.CharField(db_column='Race Category', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ethnicity = models.CharField(db_column='Ethnicity', max_length=100)  # Field name made lowercase.
    ethnicity_category = models.CharField(db_column='Ethnicity Category', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    language = models.CharField(db_column='Language', max_length=100)  # Field name made lowercase.
    inactive = models.CharField(db_column='Inactive', max_length=3)  # Field name made lowercase.
    registration_date = models.DateTimeField(db_column='Registration Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    has_duplicates = models.CharField(db_column='Has Duplicates', max_length=3)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    active_inactive = models.CharField(db_column='Active/InActive', max_length=8, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    inactivity_reason = models.CharField(db_column='InActivity Reason', max_length=15, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    inactive_comments = models.CharField(db_column='Inactive Comments', max_length=500, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date_of_death = models.DateTimeField(db_column='Date of Death', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    discontinue_statement = models.CharField(db_column='Discontinue Statement', max_length=5, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    discontinue_statement_reason = models.CharField(db_column='Discontinue Statement Reason', max_length=30, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    inactive_date = models.DateTimeField(db_column='Inactive Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.


    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'DemographicsView'


class Diagnosis(models.Model):
    practice = models.CharField(db_column='Practice', max_length=95, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=35, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    date_time = models.DateTimeField(db_column='Date / Time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_id = models.IntegerField(db_column='Patient ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_first_name = models.CharField(db_column='Patient First Name', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_last_name = models.CharField(db_column='Patient Last Name', max_length=95, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_name = models.CharField(db_column='Patient Name', max_length=146, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    description = models.TextField(db_column='Description', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    icd_10 = models.CharField(db_column='ICD-10', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    icd_9 = models.CharField(db_column='ICD-9', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    status = models.CharField(db_column='Status', max_length=8, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    onset = models.CharField(db_column='Onset', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    severity = models.CharField(db_column='Severity', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    chronic = models.CharField(db_column='Chronic', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    comments = models.TextField(db_column='Comments', db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    added_by = models.CharField(db_column='Added by', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    reason = models.CharField(db_column='Reason', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    past_current = models.CharField(db_column='Past / Current', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    significance = models.CharField(db_column='Significance', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    last_updated_by_user = models.CharField(db_column='Last Updated By User', max_length=61, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_updated_date = models.DateTimeField(db_column='Last Updated Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    data_sync_date = models.DateField(db_column='Data Sync Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Diagnosis'

class Diagnosisview(models.Model):
    date_time = models.DateTimeField(db_column='Date / Time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_id = models.ForeignKey(Demographicsview, db_column='Patient ID', primary_key=True, on_delete=models.PROTECT, related_name='diagnosis')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_first_name = models.CharField(db_column='Patient First Name', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    icd_10 = models.CharField(db_column='ICD-10', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    icd_9 = models.CharField(db_column='ICD-9', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    status = models.CharField(db_column='Status', max_length=8)  # Field name made lowercase.
    onset = models.CharField(db_column='Onset', max_length=150)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50)  # Field name made lowercase.
    severity = models.CharField(db_column='Severity', max_length=50)  # Field name made lowercase.
    chronic = models.CharField(db_column='Chronic', max_length=3)  # Field name made lowercase.
    comments = models.TextField(db_column='Comments')  # Field name made lowercase.
    past_current = models.CharField(db_column='Past / Current', max_length=20, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'DiagnosisView'

class Notesview(models.Model):
    patient_id = models.ForeignKey(Demographicsview, db_column='Patient ID', on_delete=models.PROTECT, related_name='notes', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    note_id = models.IntegerField(db_column='Note ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_first_name = models.CharField(db_column='Patient First Name', max_length=50, null=True, blank=True)
    visit_reason = models.CharField(db_column='Visit Reason', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    note_template = models.CharField(db_column='Note Template', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    note_type = models.CharField(db_column='Note type', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    created_date_and_time = models.DateTimeField(db_column='Created Date And time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    age_group_2 = models.CharField(db_column='Age Group 2', max_length=8)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    diagnosis_attached = models.CharField(db_column='Diagnosis Attached', max_length=3)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    diagnosis_codes = models.TextField(db_column='Diagnosis Codes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    procedure_codes = models.TextField(db_column='Procedure Codes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    soaptext = models.TextField(db_column='SOAPTEXT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'NotesView'


class Orders(models.Model):
    practice = models.CharField(db_column='Practice', max_length=95, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    orderno = models.CharField(db_column='OrderNo', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    order_date_time = models.DateTimeField(db_column='Order Date/Time')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_id = models.IntegerField(db_column='Patient ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_first_name = models.CharField(db_column='Patient First Name', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_last_name = models.CharField(db_column='Patient Last Name', max_length=95, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    laboratory = models.CharField(db_column='Laboratory', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ordering_provider = models.CharField(db_column='Ordering Provider', max_length=126, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cpt_description = models.CharField(db_column='CPT Description', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lab_test_description = models.CharField(db_column='Lab Test Description', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cpt = models.CharField(db_column='CPT', max_length=17, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    lab_code = models.CharField(db_column='Lab Code', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    status = models.CharField(db_column='Status', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    referred_to = models.CharField(db_column='Referred To', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    type = models.CharField(db_column='Type', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    attached_in_note = models.CharField(db_column='Attached in Note', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    note_id = models.IntegerField(db_column='Note ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    diagnosis_attached = models.CharField(db_column='Diagnosis Attached', max_length=2000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ordered_in_curemd = models.CharField(db_column='Ordered in CureMD', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    specimen_type = models.CharField(db_column='Specimen Type', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    create_date = models.DateTimeField(db_column='Create Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    update_date = models.DateTimeField(db_column='Update Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    radiology_result = models.CharField(db_column='Radiology Result', max_length=8000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    urgency_level = models.CharField(db_column='Urgency Level', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    collection_date = models.DateTimeField(db_column='Collection Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    specimen_source = models.CharField(db_column='Specimen Source', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_account_no = models.CharField(db_column='Patient Account No', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    internal_test_comments = models.TextField(db_column='Internal Test Comments', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Orders'


class Ordersview(models.Model):
    orderno = models.CharField(db_column='OrderNo', max_length=50, primary_key=True)  # Field name made lowercase.
    order_date_time = models.DateTimeField(db_column='Order Date/Time')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_id = models.ForeignKey(Demographicsview, db_column='Patient ID', on_delete=models.PROTECT, related_name='orders')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cpt_description = models.CharField(db_column='CPT Description', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lab_test_description = models.CharField(db_column='Lab Test Description', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cpt = models.CharField(db_column='CPT', max_length=17, blank=True, null=True)  # Field name made lowercase.
    lab_code = models.CharField(db_column='Lab Code', max_length=500, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    status = models.CharField(db_column='Status', max_length=15, blank=True, null=True)  # Field name made lowercase.
    note_id = models.ForeignKey(Notesview, db_column='Note ID', blank=True, null=True, on_delete=models.PROTECT)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    diagnosis_attached = models.CharField(db_column='Diagnosis Attached', max_length=2000, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    radiology_result = models.CharField(db_column='Radiology Result', max_length=8000, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    urgency_level = models.CharField(db_column='Urgency Level', max_length=30, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    internal_test_comments = models.TextField(db_column='Internal Test Comments', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'OrdersView'


class PatientDemographics(models.Model):
    server_name = models.CharField(db_column='Server Name', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dbname = models.CharField(db_column='DBNAME', max_length=14, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    pracname = models.CharField(db_column='PracName', max_length=95, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    patientid = models.IntegerField(db_column='PatientID')  # Field name made lowercase.
    account_number = models.CharField(db_column='Account Number', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gender = models.CharField(db_column='Gender', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    date_of_birth = models.DateTimeField(db_column='Date of Birth', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    age_in_years = models.IntegerField(db_column='Age in Years', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    age_in_months = models.IntegerField(db_column='Age in Months', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    age_in_weeks = models.IntegerField(db_column='Age in Weeks', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    age_in_days = models.IntegerField(db_column='Age in Days', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    age_uds = models.IntegerField(db_column='Age UDS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    age_in_years_uds = models.CharField(db_column='Age in Years UDS', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    age_group = models.CharField(db_column='Age Group', max_length=7, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    age_group_2 = models.CharField(db_column='Age Group 2', max_length=8, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    age_group_3 = models.CharField(db_column='Age Group 3', max_length=8, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    age_group_4 = models.CharField(db_column='Age Group 4', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    marital_status = models.CharField(db_column='Marital Status', max_length=9, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    race = models.TextField(db_column='Race', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    race_category = models.CharField(db_column='Race Category', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ethnicity = models.CharField(db_column='Ethnicity', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ethnicity_category = models.CharField(db_column='Ethnicity Category', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    language = models.CharField(db_column='Language', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    inactive = models.CharField(db_column='Inactive', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    red_flagged = models.CharField(db_column='Red Flagged', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    red_flag_reason = models.CharField(db_column='Red Flag Reason', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    demographics_comments = models.CharField(db_column='Demographics Comments', max_length=2000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    registration_date = models.DateTimeField(db_column='Registration Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sliding_scale_applies = models.CharField(db_column='Sliding Scale Applies', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    household_size = models.IntegerField(db_column='Household Size')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    income = models.FloatField(db_column='Income')  # Field name made lowercase.
    income_as_percentage_of_poverty_level = models.CharField(db_column='Income as Percentage of Poverty Level', max_length=14, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    income_as_percentage_of_poverty_level_2 = models.CharField(db_column='Income as Percentage of Poverty Level 2', max_length=14, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    income_as_percentage_of_poverty_level_3 = models.CharField(db_column='Income as Percentage of Poverty Level 3', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    income_as_percentage_of_poverty_level_4 = models.CharField(db_column='Income as Percentage of Poverty Level 4', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    migratory = models.CharField(db_column='Migratory', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    seasonal = models.CharField(db_column='Seasonal', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    school_based_health_center_patient = models.CharField(db_column='School Based Health Center Patient', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    homeless_type = models.CharField(db_column='Homeless Type', max_length=16, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    veteran = models.CharField(db_column='Veteran', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    patient_agency = models.CharField(db_column='Patient Agency', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    has_duplicates = models.CharField(db_column='Has Duplicates', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sexual_orientaion = models.CharField(db_column='Sexual Orientaion', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gender_identity = models.CharField(db_column='Gender Identity', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    referral_sources = models.CharField(db_column='Referral Sources', max_length=8000, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_updated_date = models.DateTimeField(db_column='Last Updated Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    active_inactive = models.CharField(db_column='Active/InActive', max_length=8, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    inactivity_reason = models.CharField(db_column='InActivity Reason', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    inactive_comments = models.CharField(db_column='Inactive Comments', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_portal_account = models.CharField(db_column='Patient Portal Account', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date_of_death = models.DateTimeField(db_column='Date of Death', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    county_name = models.CharField(db_column='County Name', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    public_housing = models.CharField(db_column='Public Housing', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    jail = models.CharField(db_column='Jail', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    prison = models.CharField(db_column='Prison', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    nursing_home = models.CharField(db_column='Nursing Home', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_portal_login_time = models.DateTimeField(db_column='Patient Portal Login Time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    limited_english_proficiency = models.CharField(db_column='Limited English Proficiency', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    discontinue_statement = models.CharField(db_column='Discontinue Statement', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    exempt_from_reporting = models.CharField(db_column='Exempt From Reporting', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hisexempt = models.CharField(db_column='HISExempt', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    age_group_std = models.CharField(db_column='Age Group STD', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    suffix = models.CharField(db_column='Suffix', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    discontinue_statement_reason = models.CharField(db_column='Discontinue Statement Reason', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    inactive_date = models.DateTimeField(db_column='Inactive Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Patient Demographics'


class Preauthorization(models.Model):
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    insurancecompany = models.CharField(db_column='InsuranceCompany', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    patientname = models.CharField(db_column='PatientName', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    policyholdername = models.CharField(db_column='PolicyHolderName', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    patientid = models.CharField(db_column='PatientID', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    policyclaim = models.CharField(db_column='PolicyClaim', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    surgerydate = models.DateField(db_column='SurgeryDate', blank=True, null=True)  # Field name made lowercase.
    policynamenumber = models.CharField(db_column='PolicyNameNumber', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    maybels = models.CharField(db_column='MayBels', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    riskfactors = models.CharField(db_column='RiskFactors', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    faxnumber = models.CharField(db_column='FaxNumber', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    telephonenumber = models.CharField(db_column='TelephoneNumber', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    physicianname = models.CharField(db_column='PhysicianName', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    practicename = models.CharField(db_column='PracticeName', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Preauthorization'


class Providernotes(models.Model):
    practice = models.CharField(db_column='Practice', max_length=95, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    patient_id = models.IntegerField(db_column='Patient ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    account_number = models.CharField(db_column='Account Number', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_first_name = models.CharField(db_column='Patient First Name', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_last_name = models.CharField(db_column='Patient Last Name', max_length=95, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    note_id = models.IntegerField(db_column='Note ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    appointment_id = models.IntegerField(db_column='Appointment ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    provider_id = models.IntegerField(db_column='Provider ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    provider = models.CharField(db_column='Provider', max_length=196, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    visit_reason = models.CharField(db_column='Visit Reason', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    note_template = models.CharField(db_column='Note Template', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location = models.CharField(db_column='Location', max_length=35, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    note_type = models.CharField(db_column='Note type', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    status = models.CharField(db_column='Status', max_length=6, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    created_date_and_time = models.DateTimeField(db_column='Created Date And time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    non_mu = models.CharField(db_column='Non-MU', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    age_group_2 = models.CharField(db_column='Age Group 2', max_length=8, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    resource = models.CharField(db_column='Resource', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    confidential = models.CharField(db_column='Confidential', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    diagnosis_attached = models.CharField(db_column='Diagnosis Attached', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    diagnosis_codes = models.TextField(db_column='Diagnosis Codes', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    procedure_codes = models.TextField(db_column='Procedure Codes', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dictation_date = models.DateTimeField(db_column='Dictation Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    soaptext = models.TextField(db_column='SOAPTEXT', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProviderNotes'


class Results(models.Model):
    practice = models.CharField(db_column='Practice', max_length=95, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    result_date_time = models.DateTimeField(db_column='Result Date/Time')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    order_no = models.CharField(db_column='Order No', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_id = models.IntegerField(db_column='Patient ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_first_name = models.CharField(db_column='Patient First Name', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_last_name = models.CharField(db_column='Patient Last Name', max_length=95, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    laboratory = models.CharField(db_column='Laboratory', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ordering_provider = models.CharField(db_column='Ordering Provider', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    test_description = models.CharField(db_column='Test Description', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cpt = models.CharField(db_column='CPT', max_length=17, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    lab_code = models.CharField(db_column='Lab Code', max_length=62, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    observation = models.CharField(db_column='Observation', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    loinc = models.CharField(db_column='LOINC', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    lab_result_code = models.CharField(db_column='Lab Result Code', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    result = models.TextField(db_column='Result', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    range = models.CharField(db_column='Range', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    flag = models.CharField(db_column='Flag', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    observation_notes = models.TextField(db_column='Observation Notes', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    status = models.CharField(db_column='Status', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    latest_result = models.CharField(db_column='Latest Result', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location = models.CharField(db_column='Location', max_length=35, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    result_state = models.CharField(db_column='Result State', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    attached_in_note = models.CharField(db_column='Attached in Note', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    note_id = models.IntegerField(db_column='Note ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    acknowledgement_time_date = models.DateTimeField(db_column='Acknowledgement Time/Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    received_time_date = models.DateTimeField(db_column='Received Time/Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    specimen_type = models.CharField(db_column='Specimen Type', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    create_date = models.DateTimeField(db_column='Create Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    update_date = models.DateTimeField(db_column='Update Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    radiology_result = models.CharField(db_column='Radiology Result', max_length=8000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_account = models.IntegerField(db_column='Patient_Account', blank=True, null=True)  # Field name made lowercase.
    data_sync_date = models.DateField(db_column='Data Sync Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Results'


class Resultsview(models.Model):
    result_date_time = models.DateTimeField(db_column='Result Date/Time')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    order_no = models.ForeignKey(Ordersview, on_delete=models.PROTECT, related_name='results', db_column='Order No', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_id = models.ForeignKey(Demographicsview, on_delete=models.PROTECT, related_name='results', db_column='Patient ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    laboratory = models.CharField(db_column='Laboratory', max_length=50, blank=True, null=True)  # Field name made lowercase.
    test_description = models.CharField(db_column='Test Description', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cpt = models.CharField(db_column='CPT', max_length=17, blank=True, null=True)  # Field name made lowercase.
    lab_code = models.CharField(db_column='Lab Code', max_length=62, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    observation = models.CharField(db_column='Observation', max_length=500)  # Field name made lowercase.
    loinc = models.CharField(db_column='LOINC', max_length=25, blank=True, null=True)  # Field name made lowercase.
    lab_result_code = models.CharField(db_column='Lab Result Code', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    result = models.TextField(db_column='Result', blank=True, null=True)  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=50, blank=True, null=True)  # Field name made lowercase.
    range = models.CharField(db_column='Range', max_length=60, blank=True, null=True)  # Field name made lowercase.
    flag = models.CharField(db_column='Flag', max_length=200, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=15, blank=True, null=True)  # Field name made lowercase.
    latest_result = models.CharField(db_column='Latest Result', max_length=3)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    note_id = models.ForeignKey(Notesview, on_delete=models.PROTECT, related_name='results', db_column='Note ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'ResultsView'


class Users(models.Model):
    username = models.CharField(db_column='Username', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    comapnyname = models.CharField(db_column='ComapnyName', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    companyaddress = models.CharField(db_column='CompanyAddress', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    zipcode = models.CharField(db_column='ZIPCode', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    emailaddress = models.CharField(db_column='EmailAddress', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Users'


class Vitals(models.Model):
    server_name = models.CharField(db_column='Server Name', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dbname = models.CharField(db_column='DBNAME', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    practice = models.CharField(db_column='Practice', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    vitalsid = models.CharField(db_column='VitalsID', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    date_time = models.CharField(db_column='Date/Time', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patientid = models.CharField(db_column='PatientID', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    patientfirstname = models.CharField(db_column='PatientFirstName', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    patientlastname = models.CharField(db_column='PatientLastName', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    weight = models.CharField(db_column='Weight', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    height = models.CharField(db_column='Height', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    waist = models.CharField(db_column='Waist', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    neck = models.CharField(db_column='Neck', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bmi = models.CharField(db_column='BMI', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bsa = models.CharField(db_column='BSA', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    leanbodyweight = models.CharField(db_column='LeanBodyWeight', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    idealbodyweight = models.CharField(db_column='IdealBodyWeight', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    oxygensaturation = models.CharField(db_column='OxygenSaturation', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    peakexpiratoryflow = models.CharField(db_column='PeakExpiratoryFlow', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    inspiredoxygenfraction = models.CharField(db_column='InspiredOxygenFraction', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bloodtype = models.CharField(db_column='BloodType', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bloodrh = models.CharField(db_column='BloodRh', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fingerstick = models.CharField(db_column='FingerStick', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    severityofpain = models.CharField(db_column='SeverityofPain', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    urineoutput = models.CharField(db_column='UrineOutput', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    latestrecord = models.CharField(db_column='LatestRecord', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pulse = models.CharField(db_column='Pulse', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    respiration = models.CharField(db_column='Respiration', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    temperature = models.CharField(db_column='Temperature', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    systolic = models.CharField(db_column='Systolic', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    diastolic = models.CharField(db_column='Diastolic', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    noteid = models.CharField(db_column='NoteID', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdate = models.CharField(db_column='CreateDate', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    updatedate = models.CharField(db_column='UpdateDate', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Vitals'


class Vitalsview(models.Model):
    vitalsid = models.CharField(primary_key=True, db_column='VitalsID', max_length=500)  # Field name made lowercase.
    date_time = models.CharField(db_column='Date/Time', max_length=500, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patientid = models.ForeignKey(Demographicsview, on_delete=models.PROTECT, related_name='vitals', db_column='PatientID', max_length=500, blank=True, null=True)  # Field name made lowercase.
    weight = models.CharField(db_column='Weight', max_length=500, blank=True, null=True)  # Field name made lowercase.
    height = models.CharField(db_column='Height', max_length=500, blank=True, null=True)  # Field name made lowercase.
    waist = models.CharField(db_column='Waist', max_length=500, blank=True, null=True)  # Field name made lowercase.
    neck = models.CharField(db_column='Neck', max_length=500, blank=True, null=True)  # Field name made lowercase.
    bmi = models.CharField(db_column='BMI', max_length=500, blank=True, null=True)  # Field name made lowercase.
    bsa = models.CharField(db_column='BSA', max_length=500, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=500, blank=True, null=True)  # Field name made lowercase.
    leanbodyweight = models.CharField(db_column='LeanBodyWeight', max_length=500, blank=True, null=True)  # Field name made lowercase.
    idealbodyweight = models.CharField(db_column='IdealBodyWeight', max_length=500, blank=True, null=True)  # Field name made lowercase.
    latestrecord = models.CharField(db_column='LatestRecord', max_length=500, blank=True, null=True)  # Field name made lowercase.
    pulse = models.CharField(db_column='Pulse', max_length=500, blank=True, null=True)  # Field name made lowercase.
    respiration = models.CharField(db_column='Respiration', max_length=500, blank=True, null=True)  # Field name made lowercase.
    temperature = models.CharField(db_column='Temperature', max_length=500, blank=True, null=True)  # Field name made lowercase.
    systolic = models.CharField(db_column='Systolic', max_length=500, blank=True, null=True)  # Field name made lowercase.
    diastolic = models.CharField(db_column='Diastolic', max_length=500, blank=True, null=True)  # Field name made lowercase.
    noteid = models.ForeignKey(Notesview, on_delete=models.PROTECT, related_name='vitals', db_column='NoteID', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'VitalsView'


class PreauthorizationRequests(models.Model):
    provider_name = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    provider_address = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    provider_email = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    provider_phone = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    insurance_company_name = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    insurance_department = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    insurance_address = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    subject = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    policy_holder_name = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    policy_number = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    patient_name = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    patient_dob = models.DateField(blank=True, null=True)
    proposed_date_of_service = models.DateField(blank=True, null=True)
    procedure_description = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # This field type is a guess.
    medical_necessity = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # This field type is a guess.
    expected_benefits = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # This field type is a guess.
    cost_estimates = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    attachments = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    contact_phone = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    contact_email = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'preauthorization_requests'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)
