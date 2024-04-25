"""
URL configuration for backend_dews project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# backend_dews/urls.py
from django.urls import path
from .views.student_list_view import student_list_view
from .views.showPredictionsBaseline1 import predictions_view, single_student_prediction_view


urlpatterns = [
    path('students/', student_list_view, name='student_list'),
    path('predictions/', predictions_view, name='predictions'),
    path('predictions/<str:student_id>/', single_student_prediction_view, name='single_student_prediction'),

    # Add more URL patterns as needed
]

