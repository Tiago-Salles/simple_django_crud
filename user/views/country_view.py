from user.models.country_model import Country
from rest_framework.decorators import api_view
from rest_framework.response import Response

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

 
@api_view(['POST'])
def create_new_country(request):
 print(request.data)
 Country.manager.create_country(
  country_name=request.data["country"],
  language=request.data["language"],
 )
 return Response(request.data)