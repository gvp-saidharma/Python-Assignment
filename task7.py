# 7-Write a program to access only unique key value of a Python object.

import json
json_obj =  '{ "Name":"Sai", "Designation":"Associate Consultant", "Age":30, "Name": "Dharma" }'
print("Original Python object:", json_obj)

obj = json.loads(json_obj)
print("Unique Key in a JSON object:", obj)
