import openai
import os 

key = os.environ.get('key')
openai.api_key = key
class DataFilter:

    def __init__(self, data):
        self.data  = data
        self.data = self.valid_python_dict()
        self.extract_details()

    def valid_python_dict(self):
        return eval(self.data.replace("null","None"))

    def extract_personal_info(self):
        personal_info = {}
        personal_info['name'] = self.data['notes'][0]['patient_first_name']
        personal_info['age'] = self.data['age_in_years']
        personal_info['marital_status'] = self.data['marital_status']
        if self.data['date_of_death']: personal_info['date_of_death'] = self.data['date_of_death']

        return personal_info

    def extract_property_details(self, property):
        if property == 'results':
            if len(self.data['orders']) >1:
                if 'results' in self.data['orders'][0].keys() and len(self.data['orders'][0]['results']) > 1:
                    return self.data['orders'][0]['results'][0]
                else:
                    return None
            else:
                return None
        elif self.data[property]:
            prop = self.data[property][0].copy()
            if property == 'orders' and prop['results']:
                prop.pop('results')
            return prop
        else:
            return None  

    def extract_details(self):
        self.personal_info = self.extract_personal_info()
        self.orders  =    self.extract_property_details('orders')
        self.results  =    self.extract_property_details('results')
        self.vitals  =    self.extract_property_details('vitals')
        self.notes  =    self.extract_property_details('notes')
        self.diagnosis  =    self.extract_property_details('diagnosis')


class ChatGPT(DataFilter):

    def __init__(self,data):
        super().__init__(data =data)
        self.context = []
   
    def generate_prompt(self):
        self.converse("Please act like a doctor, I'm going to give you a some data and you should not respond any message until I want you to.")
        self.converse(f"Here is a patient and his personal information: {self.personal_info}, Please remember this")
        self.converse(f"Here are the patient's some other information: {self.notes}, please remember this also")
        if self.orders:
            self.converse(f"Here are some lab orders for the patient: {self.orders}. Please remember this also")
        if self.results:
            self.converse(f"Here are some lab results against the orders I provided you for the patient: {self.results}. Please remember this also")
        if self.vitals:
            self.converse(f"Here are vitals of the patient recorded: {self.vitals}. Please remember this also")
        if self.diagnosis:
            self.converse(f"Here are some Diagnosis of the patient: {self.diagnosis}. Please remember this also")

        resp = self.converse("Please Provide a very Descriptive Clinical Progress Note with small summary at the end in html format for all the information I have provided you.")
        
        return resp.split("```")[1].replace("\n", "")

    def starter(self,model = 'gpt-3.5-turbo-0613'):
        response = openai.ChatCompletion.create(
            model = model,
            messages = self.context,
            temperature =0.5
        )
        return response.choices[0].message['content']

    def converse(self,prompt):
        self.context.append({"role":"user", "content":f"{prompt}"})
        response = self.starter()
        self.context.append({"role":"assistant", "content":f"{response}"})
        return response