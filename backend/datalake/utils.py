
from rest_framework.utils.serializer_helpers import ReturnList
from rest_framework.utils.serializer_helpers import ReturnDict
from collections import OrderedDict

def clean_response_data(data):
    if isinstance(data, str):
        data = data.strip()
    elif isinstance(data, ReturnList):
        for item in data:
            clean_response_data(item)
    elif isinstance(data, ReturnDict):
        for key in data:
            clean_response_data(data[key])
    elif isinstance(data, OrderedDict):
        for key in data:
            data[key] = clean_response_data(data[key])
    
    return data
