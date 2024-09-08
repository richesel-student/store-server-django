from django.urls import path

from products.views import products

app_name = 'products'

urlpatterns = [
    path('', products, name='index')
]
# from django.urls import path
#
# from users.views import login, registration, profile
#
#
#
# app_name = 'users'
#
# urlpatterns = [
#     path('login/', login, name='login'),
#     path('registration/', registration, name='registration'),
#     path('profile/', profile, name='profile'),
# ]