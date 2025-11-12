import json
json_string = '{"ism": "Umid", "yosh": 25}'
python_obj = json.loads(json_string)
print(python_obj)
print(python_obj['ism'])