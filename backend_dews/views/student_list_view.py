# your_django_app/views/student_views.py
from django.http import JsonResponse
from elasticsearch_utils.queries import search_documents

def student_list_view(request):
    # Fetch student data from Elasticsearch
    es_query = {
        "query": {
            "match_all": {}
        }
    }
    es_results = search_documents('data_middle_1', es_query)  # Update index name accordingly
    student_data = [hit['_source'] for hit in es_results]

    # Render data in JSON response
    return JsonResponse(student_data, safe=False)
