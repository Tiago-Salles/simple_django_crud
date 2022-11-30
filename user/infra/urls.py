from django.urls import path
from ..views.country_view import *

urlpatterns =[
 path("all/", get_all_countries, name="countries"),
 path("create/", create_new_country, name="new_country")
]