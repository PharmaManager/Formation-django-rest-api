from api.models import Product
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']
        
    def create(self, validated_data):
        
        email = validated_data.pop('email', None)
        print(f"Email received during product creation: {email}")
        return super().create(validated_data)