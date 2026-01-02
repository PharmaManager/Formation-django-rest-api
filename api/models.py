from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
            ordering = ['-created_at']

    def get_price_in_euros(self):
        return f'{self.price} €'
    
    def get_description(self):
        return f'Description: {self.name} - {self.price} €'
    def __str__(self):
        return self.name
    

    
    