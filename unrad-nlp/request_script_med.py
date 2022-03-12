import requests
import credentials
import json
import os

base = "https://language.googleapis.com"
# "https://healthcare.googleapis.com/v1/{nlpService=projects/*/locations/*/services/nlp}:analyzeEntities"
#base = 'https://healthcare.googleapis.com'

# dictation content
with open('../docs/plaintext/abdomen-mri-with-contrast-sample-report-1.txt') as f:
    text = f.read()

# API key
# with open('../../radiology-unstructured-text-4280fe5918b0.json')
with open('../../api_radiology_unstructured_text.txt') as f:
    API_KEY = f.read()

# API call
doc = {"type": "PLAIN_TEXT", "content": text}
request_data = {"document" : doc, "encodingType": "UTF8"}

# projects/projectId/locations/locationId/services/nlp


# needs updating to medical
#analysis_endpoint = "/v1/documents:analyzeSyntax"
#analysis_url = base + analysis_endpoint + "?key=" + credentials.API_KEY

entities_endpoint = "/v1/documents:analyzeEntities"
entities_url = base + entities_endpoint + "?key=" + API_KEY

response = requests.post(entities_url, data = json.dumps(request_data))
entities_results = json.loads(response.text)
print(json.dumps(entities_results, indent=4))

file_dir = '../docs/responses/entities_1.json'
os.makedirs(os.path.dirname(file_dir))

with open('../docs/responses/entities_1.json', 'w') as outfile:
    outfile.write(json.dumps(response.json()))
