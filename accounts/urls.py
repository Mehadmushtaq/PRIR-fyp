from django.urls import path
from accounts.views import *

urlpatterns = [
   path('login/' , login_page , name="login" ),
   path('register/' , register_page , name="register"),
   path('logout/' , signOut , name="logout"),
   path('brand/' , brand , name="brand"),
   path('brand-login/' , brand_login , name="brand_login"),
   path('activate/<email_token>/' , activate_email , name="activate_email"),
   path('add-to-cart/<uid>/', add_to_cart, name="add_to_cart"),
   path('cart/', cart, name="cart"),
   path('remove-cart/<uid>/', remove_cart, name="remove_cart")
]
