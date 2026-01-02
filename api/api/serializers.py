from api.models import Product
from rest_framework import serializers

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    
    vendor_product = serializers.PrimaryKeyRelatedField(many=True, read_only=True,source='vendor_products')
    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name', 'vendor_product']

class ProductSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)
    link = serializers.HyperlinkedIdentityField(view_name='api:product-detail', lookup_field='pk')
    vendor = UserSerializer(read_only=True)
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at', 'link']
        
    def create(self, validated_data):
        
        email = validated_data.pop('email', None)
        print(f"Email received during product creation: {email}")
        user = self.context['request'].user

        print(f"Authenticated user: {user} and email: {email}")
        validated_data['vendor'] = user
        return super().create(validated_data)
    def validate_name(self, value):
        if value in ['komi', 'komi-san']:
            raise serializers.ValidationError("This product name is not allowed.")
        return value