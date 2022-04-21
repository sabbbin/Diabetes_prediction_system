from django.urls import path
from predictor import views

urlpatterns = [
    path('', views.prediction, name='predict'),
    path('result/', views.process, name='process'),   
]
