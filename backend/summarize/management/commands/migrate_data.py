from typing import Any, Optional
from django.core.management.base import BaseCommand, CommandParser
import pandas as pd
from summarize.models import * 
from summarize.serializers import * 
from medistream.settings import REMOTE_DATABASES
from getpass import getpass
import sqlite3
import pyodbc
import os 
from sqlalchemy import create_engine, text 


class Command(BaseCommand):
    help = 'this command takes raw data from db server and converts it to structured data and store it to database used with this backend'

    _TABLE_NAMES = {
        # 'Demographics': 'summarize_patientdemographics',
        # 'DiagnosisView': 'summarize_diagnosis',
        'NotesView': 'summarize_providernote',
        'VitalsView': 'summarize_vital',
        'OrdersView': 'summarize_order',
        'ResultsView': 'summarize_result',
    }

    _SERIALIZERS_DICT = {
        'Demographics': PatientDemographicsSerializer,
        'DiagnosisView': DiagnosisSerializer,
        'NotesView': ProviderNoteSerializer,
        'VitalsView': VitalSerializer,
        'OrdersView': OrderSerializer,
        'ResultsView': ResultSerializer,
    }

    def handle(self, *args: Any, **options: Any) -> str | None:
        server = 'CMDLHRDB01'
        database = 'One Practice Sample'
        trusted_connection = 'yes'
        cnxn = pyodbc.connect(
            'DRIVER={SQL Server};' + f'SERVER={server};DATABASE={database};TRUSTED_CONNECTION={trusted_connection}'
        )
        
        for key in self._TABLE_NAMES.keys():
        
            query = f'SELECT  * FROM [One Practice Sample ].[dbo].[{key}]'
            df = pd.read_sql(query, cnxn)

            _column_mappings = dict(map(
                lambda col: (col, col.lower()
                             .replace(' ', '_')
                             .replace(' / ', '_')
                             .replace('/', '_')),
                df.columns))
            if 'PatientID' in _column_mappings:
                _column_mappings['PatientID'] = 'patient_id'
            if 'SOAPTEXT' in _column_mappings:
                _column_mappings['SOAPTEXT'] = 'soap_text'
            if key != 'Demographics' and 'Patient ID' in _column_mappings:
                _column_mappings['Patient ID'] = 'patient'
            # print(_column_mappings)
            
            df.rename(columns=_column_mappings, inplace=True)
            df.replace({pd.NaT: None}, inplace=True)
            # print(df.columns)

            data_dict_list = df.to_dict(orient='records')


            # Deserialize objects
            for data_dict in data_dict_list:
                serializer = self._SERIALIZERS_DICT[key](data=data_dict)
                if serializer.is_valid():
                    serializer.save()
                else:
                    print(f"{self._SERIALIZERS_DICT[key].__class__} deserialization errors:", serializer.errors)
                    print(data_dict)
        cnxn.close()
        # sqlite_file = 'db.sqlite3'
        # cnxn = sqlite3.connect(sqlite_file)
        # batch_size = 10
        # for batch_start in range(0, len(df), batch_size):
        #     batch_df = df[batch_start : batch_start + batch_size]
        #     batch_df.to_sql('summarize_patientdemographics', cnxn, if_exists='append', index=False)

        #     sql = df.to_sql('summarize_patientdemographics', cnxn, if_exists='replace', index=False, method='multi')
        #     print(sql.statement)

#         database_url = 'sqlite:///db.sqlite3'
#         engine = create_engine(database_url, echo=True)
#         data_dict_list = df.to_dict(orient='records')
#         print(data_dict_list)
#         with engine.connect() as conn:
#             query = text("""
# INSERT INTO summarize_patientdemographics (patient_id, gender, date_of_birth, marital_status, race, race_category, ethnicity, ethnicity_category, language, inactive, registration_date, has_duplicates, active_inactive, inactivity_reason, inactive_comments, date_of_death, discontinue_statement, discontinue_statement_reason, 
# inactive_date) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
# """)
#             conn.execute(query, data_dict_list)

#         print(engine.url.database)
#         engine.dispose()


        # cnxn.close()

