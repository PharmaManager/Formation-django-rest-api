from api.models import Product
from api.api.serializers import ProductSerializer
from rest_framework.viewsets import ModelViewSet    
from rest_framework.routers import DefaultRouter
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin,CreateModelMixin,DestroyModelMixin,UpdateModelMixin


class ProductViewSet(ModelViewSet):
    
    pass
    queryset = Product.objects.all()
    serializer_class = ProductSerializer