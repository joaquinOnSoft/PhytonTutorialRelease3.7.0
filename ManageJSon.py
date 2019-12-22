import json

with open('example.json', 'r') as f:
    json_obj = json.load(f)
    print("JSON:", json_obj)
    print("title:", json_obj['glossary']['title'])