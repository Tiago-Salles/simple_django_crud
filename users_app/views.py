from rest_framework.decorators import api_view
from rest_framework.response import Response
from users_app.models import User 

@api_view(['GET'])
def get_all_users(request):
 response = User.manager.get_all_users()
 data = []
 for user in response:
  data.append({
    "name" : user.user_name,
    "cpf" : user.user_cpf,
    "country" : user.user_country,
    })
 return Response({"data": data})

@api_view(['POST'])
def register_user(request):
 User.manager.register_user(
  user_name=request.data.name,
  user_cpf=request.data.cpf,
  user_country=request.data.country
 )
 return request.data
