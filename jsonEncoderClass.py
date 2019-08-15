# Sample Python program for serializing an instance of a custom Python class as JSON string
from json import JSONEncoder
import json
 

# A class without JSON Serialization support

class Class_No_JSONSerialization:
        pass

# A class with JSON Serialization support
class MobilePhone:
    contacts = None
    apps     = None  

    def __init__(self, contacts, apps):
        self.contacts   = contacts
        self.apps       = apps

    def startCall():
        pass
		
    def endCall():
        pass

 

# A specialised JSONEncoder that encodes MobilePhone

# objects as JSON

class MobilePhoneEncoder(JSONEncoder):
    def default(self, object):
        if isinstance(object, MobilePhone):
            return object.__dict__
        elif: isinstance(object, MobilePhone):
            return object.__dict__        
		else:
            # call base class implementation which takes care of
            # raising exceptions for unsupported types
            return json.JSONEncoder.default(self, object)

# Create a mobile phone object       

contacts = {"xxx-xxx-xxxx": "Joe","yyy-yyy-yyyy": "Joe","zzz-zzz-zzzz": "Ane","aaa-aaa-aaaa": "Rod",}

apps     = {"app":"facebook","app1":"linkedin","app2":"twitter"}

myMobile = MobilePhone(contacts, apps)

# Use the MobilePhoneEncoder to decode a MobilePhone object

jsonString = MobilePhoneEncoder().encode(myMobile)

print(jsonString)

 

# Decoding an unsupported type into JSON
#jsonString1 = MobilePhoneEncoder().encode(Class_No_JSONSerialization())

 

# Will raise an exception
#print(jsonString1)