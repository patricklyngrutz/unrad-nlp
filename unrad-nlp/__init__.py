import json
import os
from google.cloud import language

# load api_key into memory from local
with open('../radiology-unstructured-text-4280fe5918b0.json') as f: apikey = json.load(f)

#os.environ['GOOGLE-APPLICATION_CREDENTIALS'] = 'C:\Google Drive\Data Science\Python Projects/radiology-unstructured-text-4280fe5918b0.json'
GOOGLE_APPLICATION_CREDENTIALS = apikey

# load test case
with open('./docs/plaintext/abdomen-mri-with-contrast-sample-report-1.txt') as f: dictation = f.read()

def language_analysis(text):
    client = language.LanguageServiceClient.from_service_account_json('../radiology-unstructured-text-4280fe5918b0.json')
    document = language.Document(type = 'PLAIN_TEXT',content = text)
    sen_response = client.analyze_sentiment(document = document)
    sentiment = sen_response.document_sentiment
    ent_response = client.analyze_entities(document = document)
    return sentiment, entities
