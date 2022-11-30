from django.urls import path
from users_app.views import *

urlpatterns = [
 path('all/', get_all_users, name='all_users'),
 path('register', register_user, name='register_user')
]