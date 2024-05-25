from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from elasticsearch import Elasticsearch
from django.http import JsonResponse
# from elasticsearch_utils.queries import search_documents

ELASTIC_PASSWORD = "ZkgiSTdIgawzh8--ogdY"  # Define ELASTIC_PASSWORD before using it
es_client = Elasticsearch("http://localhost:9200", http_auth=("elastic", ELASTIC_PASSWORD))

class StudentDistributionByLevel(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        try:
            body = {
                "size": 0,
                "aggs": {
                    "levels": {
                        "terms": {"field": "Level"}
                    }
                }
            }
            response = es_client.search(index="data_middle_*", body=body)
            results = response['aggregations']['levels']['buckets']
            table_data = [{"level": result['key'], "count": result['doc_count']} for result in results]
            return JsonResponse(table_data, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

