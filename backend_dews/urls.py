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
from .views.students_list import student_list
from .views.prediction_M_1_2 import (
    predictions_M_1_2Baseline,
    single_student_prediction_M_1_2Baseline,
    predictions_M_1_2Undrsampling,
    single_student_prediction_M_1_2Undrsampling,
)
from .views.prediction_M_1_1 import (
    predictions_M_1_1Baseline,
    single_student_prediction_M_1_1Baseline,
    predictions_M_1_1Undrsampling,
    single_student_prediction_M_1_1Undrsampling,
)

urlpatterns = [
    path('students/', student_list_view, name='student_list'),
    path('studentslist/', student_list, name='student_list'),
    # level 7 
    # predictions after 1 year
    path('predictions/M_1_1Baseline/', predictions_M_1_1Baseline, name='predictions_M_1_2Baseline'),
    path('predictions/M_1_1Baseline/<str:student_id>/', single_student_prediction_M_1_1Baseline, name='single_student_prediction_M_1_2Baseline'),
    path('predictions/M_1_1Undrsampling/', predictions_M_1_1Undrsampling, name='predictions_M_1_2Undrsampling'),
    path('predictions/M_1_1Undrsampling/<str:student_id>/', single_student_prediction_M_1_1Undrsampling, name='single_student_prediction_M_1_2Undrsampling'),
    # predictions after 2 years
    path('predictions/M_1_2Baseline/', predictions_M_1_2Baseline, name='predictions_M_1_2Baseline'),
    path('predictions/M_1_2Baseline/<str:student_id>/', single_student_prediction_M_1_2Baseline, name='single_student_prediction_M_1_2Baseline'),
    path('predictions/M_1_2Undrsampling/', predictions_M_1_2Undrsampling, name='predictions_M_1_2Undrsampling'),
    path('predictions/M_1_2Undrsampling/<str:student_id>/', single_student_prediction_M_1_2Undrsampling, name='single_student_prediction_M_1_2Undrsampling'),


]

