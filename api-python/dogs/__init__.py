import logging

import azure.functions as func
import os
import json
import requests

from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
from requests_toolbelt.multipart import decoder



def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    file = req.files["file"]

    print("*** filename: ", file.filename)
    # headers = {
    #     'Prediction-Key': '4a5a5bb3beef419692658918a5f4475f',
    #     'Content-Type': 'application/octet-stream'
    #     }
   
    # data = requests.post(os.environ["PREDICTION_URL"], headers=headers, data=file.stream.read())
    
    # return func.HttpResponse(
    #     json.dumps(data.json()) 
    # )

    endpoint = "https://customvisionsimplon-prediction.cognitiveservices.azure.com/"
    credentials = ApiKeyCredentials(in_headers={'Prediction-key':os.environ["PREDICTION_KEY"]})
    client = CustomVisionPredictionClient(endpoint, credentials)

    results = client.classify_image(os.environ["PROJECT_ID"], os.environ["ITERATION_NAME"], file.stream.read())

    data = []
    for prediction in results.predictions:
        data.append({
            "tagName": prediction.tag_name,
            "probability": prediction.probability 
        })

    return func.HttpResponse(
        json.dumps(['predictions': data) 
    )