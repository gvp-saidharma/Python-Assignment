# 6-Write a  program to convert JSON data to Python object. 

import json

json_obj =  '{ "Name":"Sai", "Designation":"Associate Consultant", "Age":30 }'
obj = json.loads(json_obj)

print("JSON data:", obj)
for key in obj:
    print(key, ":", obj[key])