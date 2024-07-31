# from django.shortcuts import render, redirect
# import requests
# import json
# from .forms import CityForm
# from django.http import JsonResponse


from django.shortcuts import render
from django.http import JsonResponse
import requests
import json
from .forms import CityForm
from django.conf import settings

def index(request):
    form = CityForm()
    weather_data = None  # Initialize to None

    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data['city_name']
            api_key = settings.API_KEY
            api_url =  f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

            try:
                weather_info = requests.get(api_url)
                weather_info.raise_for_status()  # Raise an exception for HTTP errors
                json_data = weather_info.json()

                # Filter the data
                weather_data = {
                    'city': json_data.get('name'),
                    'temperature': json_data['main'].get('temp'),
                    'description': json_data['weather'][0].get('description'),
                    'icon': json_data['weather'][0].get('icon')
                }

            except requests.RequestException as e:
                e = "City could not be found"
                # Handle errors appropriately
                weather_data = {'error': str(e)}
    else:
        form = CityForm()

    return render(request, "core/index.html", {"form": form, "weather_data": weather_data})



# def index(request):
#     if request.method == "POST":
#         form = CityForm(request.POST)
#         if form.is_valid():
#             city_name = form.cleaned_data['city_name']
#             api_key = "0b20af50331ca9a32ac55336de5ad0c8"
#             api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
#             weather_info = requests.get(api_url)
#             json_data = weather_info.json()
#             return JsonResponse(json_data)
#     else:
#         form = CityForm()
#     return render(request, "core/index.html", {"form":form})

