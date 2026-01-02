from api.models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from rest_framework.decorators import action
from api.api.serializers import ProductSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    
    @action(detail=False, methods=['GET'],url_path='expensive-products', url_name='expensive-products')
    def expensive_products(self, request):
        expensive_products = self.get_queryset().filter(price__gt=100)
        context = {'request': request}
        serializer = self.get_serializer(expensive_products, many=True, context=context)
        return Response(serializer.data)

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.query_params.get('q', None)
        if q is not None:
            queryset = queryset.filter(name__icontains=q)
        queryset = queryset.order_by('-created_at')

        return queryset