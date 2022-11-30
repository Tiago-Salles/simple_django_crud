from django.db import models
from .models import Country

class UserManager(models.Manager):
  def register_user(self, user_name, user_cpf, user_country):
    user = self.create(user_name=user_name, user_cpf=user_cpf, user_country=user_country)
    return user
  
  def get_all_users(self):
    users = self.all()
    return users
  
class User(models.Model):
 user_name = models.CharField(max_length=50)
 user_cpf = models.CharField(max_length=14)
 user_country = models.ForeignKey(Country, on_delete=models.CASCADE)
 
 manager = UserManager()