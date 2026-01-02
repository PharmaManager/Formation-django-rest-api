from django.urls import path
from api.api.viewset import ProductViewSet
from rest_framework.routers import DefaultRouter, SimpleRouter
router = DefaultRouter()


router.register('v1/product', ProductViewSet, basename='product')




urlpatterns = router.urls
