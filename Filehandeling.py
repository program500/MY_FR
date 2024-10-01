#python obj convert to python json convert to filewrite
import json
pythohObj = {
    "Name": "Abid", 
    "age": 20, 
    "city": "Gopalgonj", 
    "profession": ["engineer", "programmer"]
}

pythonjson = json.dumps(pythohObj, indent= 5)

print(pythonjson)

with open("python.json", "w") as pythonjsonfile: 
    json.dump(pythonjson, pythonjsonfile)
    print("Success")
with open ("python.json", 'r') as pythonjsonfile: 
    nm = json.load()
    print(nm["name"])