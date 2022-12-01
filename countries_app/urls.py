from django.urls import path
from countries_app.views import *

urlpatterns = [
 path('all/', get_all_countries, name='all_countries'),
 path('<str:countryName>/', get_country_details, name="get_country_details"),
 path('create/', create_new_country, name='new_country')
]