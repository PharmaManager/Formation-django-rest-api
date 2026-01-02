from django.urls import path
from api.api.viewset import ProductViewSet, UserViewSet
from rest_framework.routers import DefaultRouter, SimpleRouter
router = DefaultRouter()


router.register('v1/product', ProductViewSet, basename='product')
router.register('v1/user', UserViewSet, basename='user')



urlpatterns = router.urls
