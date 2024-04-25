# backend_dews/views.py

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import mlflow.sklearn
import pandas as pd
from elasticsearch_utils.utils import get_es_client
from Feature_engineering import Feature_engineering

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

    # Apply feature engineering
    df = Feature_engineering(df)

    # Make predictions
    predictions = loaded_model.predict(df)

    # Convert predictions to response format
    response_data = [{'student_id': hit['_source']['id_eleve'], 'prediction': int(predictions[i])} for i, hit in enumerate(es_data)]
    
    # Map predictions to "Success" or "Not Success"
    for data in response_data:
        data['prediction'] = "Success" if data['prediction'] == 0 else "Not Success"

    # Construct HTML response
    html_response = "<h1>Predictions</h1>"
    html_response += "<table border='1'><tr><th>Student ID</th><th>Prediction</th></tr>"
    for data in response_data:
        html_response += f"<tr><td>{data['student_id']}</td><td>{data['prediction']}</td></tr>"
    html_response += "</table>"

    # Return HTML response
    return HttpResponse(html_response)

@csrf_exempt
def single_student_prediction_view(request, student_id):
    # Load the ML model
    loaded_model = mlflow.sklearn.load_model("./Baseline")

    # Retrieve data from Elasticsearch index for the specified student
    es_client = get_es_client()
    index_name = "data_middle_1"
    es_query = {"query": {"match": {"id_eleve": student_id}}}
    es_response = es_client.search(index=index_name, body=es_query)

    # Process Elasticsearch data
    es_data = es_response['hits']['hits']
    df = pd.DataFrame([hit['_source'] for hit in es_data])

    # Apply feature engineering
    df = Feature_engineering(df)

    # Make prediction
    prediction = loaded_model.predict(df)

    # Convert prediction to response format
    prediction_result = "Success" if prediction[0] == 0 else "Not Success"

    # Construct HTML response
    html_response = f"<h1>Prediction for Student {student_id}</h1>"
    html_response += f"<p>Prediction: {prediction_result}</p>"

    # Return HTML response
    return HttpResponse(html_response)
