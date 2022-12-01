from rest_framework.decorators import api_view
from rest_framework.response import Response
from countries_app.models import Country

@api_view(['GET'])
def get_all_countries(request):
    response = Country.manager.get_all_countries()
    data = []
    for country in response:
        data.append({
            "country" : country.country_name,
            "language" : country.language
        })
    return Response({"data": data})

@api_view(['GET'])
def get_country_details(request, *args, **kwargs):
    country = Country.manager.get_country_details(kwargs["countryName"])
    data = {
        "country": country.country_name,
        "language": country.language,
    }
    return Response({"data" : data})

 
@api_view(['POST'])
def create_new_country(request):
    Country.manager.create_country(
     country_name=request.data["country"],
     language=request.data["language"],
    )
    return Response(request.data)