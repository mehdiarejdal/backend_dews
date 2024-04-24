# backend_dews/views.py

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import mlflow.sklearn
import pandas as pd
from elasticsearch_utils.utils import get_es_client

@csrf_exempt
def predictions_view(request):
    # Load the ML model
    loaded_model = mlflow.sklearn.load_model("./Baseline")

    # Retrieve data from Elasticsearch index
    es_client = get_es_client()
    index_name = "data_middle_1"
    es_query = {"query": {"match_all": {}}}
    es_response = es_client.search(index=index_name, body=es_query)

    # Process Elasticsearch data
    es_data = es_response['hits']['hits']
    df = pd.DataFrame([hit['_source'] for hit in es_data])

    # Make predictions
    predictions = loaded_model.predict(df)

    # Convert predictions to response format
    response_data = [{'student_id': es_data[i]['_id'], 'prediction': int(predictions[i])} for i in range(len(predictions))]

    # Construct HTML response
    html_response = "<h1>Predictions</h1>"
    html_response += "<table border='1'><tr><th>Student ID</th><th>Prediction</th></tr>"
    for data in response_data:
        html_response += f"<tr><td>{data['student_id']}</td><td>{data['prediction']}</td></tr>"
    html_response += "</table>"

    # Return HTML response
    return HttpResponse(html_response)
