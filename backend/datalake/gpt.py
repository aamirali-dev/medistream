import openai
import os

# Get the OpenAI API key from the environment variable 'key'
key = os.environ.get('key')

# Set the OpenAI API key
openai.api_key = key


class DataFilter:
    """
    A class for filtering and extracting data from a Python dictionary.

    Attributes:
        data (dict): The input data dictionary.

    Methods:
        __init__(self, data): Constructor to initialize the DataFilter instance.
        valid_python_dict(self): Validates and returns a Python dictionary.
        extract_personal_info(self): Extracts personal information from the data.
        extract_property_details(self, property): Extracts specific property details from the data.
        extract_details(self): Extracts various details from the data.

    """

    def __init__(self, data):
        """
        Initializes a DataFilter instance with the provided data.

        Args:
            data (str): A JSON-like string containing data.
        """
        self.data = data
        self.data = self.valid_python_dict()
        self.extract_details()

    def valid_python_dict(self):
        """
        Replaces "null" in string returned by database with "None" and convert to valid
        python dictionary
        Returns:
            dict: A valid Python dictionary.
        """
        return eval(self.data.replace("null", "None"))

    def extract_personal_info(self):
        personal_info = {}
        personal_info['name'] = self.data['notes'][0]['patient_first_name']
        personal_info['age'] = self.data['age_in_years']
        personal_info['marital_status'] = self.data['marital_status']
        if self.data['date_of_death']: personal_info['date_of_death'] = self.data['date_of_death']

        return personal_info

    def extract_property_details(self, property):
        """
            Filters out the data from dict based on property
        Args:
            property (str): The property name to be filtered
        Returns:
            dict or None: A dictionary containing the extracted property details if the conditions are met,
                      or None if the property does not exist or the conditions are not satisfied
        """
        if property == 'results':
            if len(self.data['orders']) > 1:
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
        """
        Extracts various details from the data and assigns them to instance attributes.

        This method invokes several other methods to extract specific details from the data and assigns them
        to instance attributes for convenient access. The extracted details include personal information, orders,
        results, vitals, notes, and diagnosis.

        Returns:
            None
        """
        self.personal_info = self.extract_personal_info()
        self.orders = self.extract_property_details('orders')
        self.results = self.extract_property_details('results')
        self.vitals = self.extract_property_details('vitals')
        self.notes = self.extract_property_details('notes')
        self.diagnosis = self.extract_property_details('diagnosis')


class ChatGPT(DataFilter):
    """
    A class that extends DataFilter and interacts with the OpenAI Chat API to generate responses.

    Attributes:
        data (dict): The input data dictionary.
        context (list): A list of conversation messages.

    Methods:
        __init__(self, data): Constructor to initialize the ChatGPT instance.
        generate_prompt(self): Generates a conversation prompt based on the provided data.
        starter(self, model): Starts a conversation with the GPT model and gets the response.
        converse(self, prompt): Adds a user message to the conversation and gets the assistant's response.

    """

    def __init__(self, data):
        """
        Initializes a ChatGPT instance with the provided data.

        Args:
            data (str): A JSON-like string containing data.
        """
        super().__init__(data=data)
        self.context = []

    def generate_prompt(self):
        """
        Generates a conversation prompt based on the provided data.

        Returns:
            str: The Final Chat GPT response with HTML Note.
        """
        # start conversation with ChatGPT
        self.converse(
            "Please act like a doctor, I'm going to give you a some data and you should not respond any message until I want you to.")

        # send personal information of patient
        self.converse(f"Here is a patient and his personal information: {self.personal_info}, Please remember this")


        # Send Note information
        self.converse(f"Here are the patient's some other information: {self.notes}, please remember this also")

        #Check if infromation exists, if yes then sends to ChatGPT
        if self.orders:
            self.converse(f"Here are some lab orders for the patient: {self.orders}. Please remember this also")
        if self.results:
            self.converse(
                f"Here are some lab results against the orders I provided you for the patient: {self.results}. Please remember this also")
        if self.vitals:
            self.converse(f"Here are vitals of the patient recorded: {self.vitals}. Please remember this also")
        if self.diagnosis:
            self.converse(f"Here are some Diagnosis of the patient: {self.diagnosis}. Please remember this also")

        #Final Response of ChatGPT in HTML Format
        resp = self.converse(
            "Please Provide a very Descriptive Clinical Progress Note with small summary at the end in html format for all the information I have provided you.")

        return resp.split("```")[1].replace("\n", "")

    def starter(self, model='gpt-3.5-turbo-0613'):
        """
        Starts a conversation with the GPT model and gets the response.

        Args:
            model (str): The GPT model to use for the conversation.

        Returns:
            str: The response from the GPT model.
        """
        response = openai.ChatCompletion.create(
            model=model,
            messages=self.context,
            temperature=0.5
        )
        return response.choices[0].message['content']

    def converse(self, prompt):
        """
        Adds a user message to the conversation and gets the assistant's response.

        Args:
            prompt (str): The user's message.

        Returns:
            str: The assistant's response.
        """
        self.context.append({"role": "user", "content": f"{prompt}"})
        response = self.starter()
        self.context.append({"role": "assistant", "content": f"{response}"})
        return response
