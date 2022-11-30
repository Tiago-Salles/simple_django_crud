from django.urls import path
from .views import *

urlpatterns = [
 path('all/', get_all_users, name='all_users'),
 path('register', register_user, name='register_user')
]