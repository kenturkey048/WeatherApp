from . import views
from django.urls import path




urlpatterns = [
    path('', views.index, name='index'),
    # path("weather-info/", views.weather_info, name='weather_details')
]