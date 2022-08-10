import json

def extractArgumentsFromJson(jsonString):
    loadedJson =json.loads(jsonString)
    return dict(loadedJson)

print(extractArgumentsFromJson('{"name":"Rupert", "age": 25, "desig":"developer"}'))
