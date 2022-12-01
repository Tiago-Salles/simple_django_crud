from rest_framework.decorators import api_view
from rest_framework.response import Response
from users_app.models import User 
from countries_app.models import Country

@api_view(['GET'])
def get_all_users(request):
  response = User.manager.get_all_users()
  data = []
  for user in response:
   data.append({
     "id" : user.id,
     "name" : user.user_name,
     "cpf" : user.user_cpf,
     "country" : {
       "countryName" : user.user_country.country_name,
       "language" :  user.user_country.language,
       },
     })
  return Response({"data": data})

@api_view(['POST'])
def register_user(request):
  country = Country.manager.country_details(request.data["country"])
  User.manager.register_user(
   user_name=request.data["name"],
   user_cpf=request.data["cpf"],
   user_country=country
  )
  return Response(request.data)

@api_view(['GET'])
def get_user_details(request, *args, **kwargs):
  user = User.manager.get_user_details(kwargs["userId"])
  data = {
      "id": user.id,
      "name": user.user_name,
      "cpf": user.user_cpf,
      "country": {
          "countryName": user.user_country.country_name,
          "language":  user.user_country.language,
      },
  }
  return Response({"data" : data})

