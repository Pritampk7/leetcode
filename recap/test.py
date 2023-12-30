data = {"data": ['Annotation', "Swamiji’s book, The Legend of the Goddess,"]}
import json

tojason = json.dumps(data, indent=4)
print(tojason)

try:
    json_output = json.dumps(data)
    print(json_output)
except Exception as e:
    print(f"An error occurred: {e}")