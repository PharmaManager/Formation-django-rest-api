from django.urls import path,include
from .views import home
from .api.api import product_api_view
from api.api.mixins import ProductViewSet
from rest_framework.authtoken.views import obtain_auth_token
 
app_name = 'api'

urlpatterns = [
   path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
   path("",home, name='home'),
   path("products/",product_api_view, name='products'),
   path("products/<int:pk>/",product_api_view, name='product_api_view'),

   path("products/<int:pk>/",product_api_view, name='product-detail'),
   path("v2/product/",ProductViewSet.as_view({'get': 'list'}), name='product-list'),
   path("",include('api.routers')),
   

]