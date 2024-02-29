from django.conf import settings
from rest_framework import serializers

from .models import ProductVariant,Product

from memory_profiler import profile
from .utils import calculate_batch_size

class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = ['sku', 'name', 'price', 'details']

class ProductSerializer(serializers.ModelSerializer):
    variants = ProductVariantSerializer(many=True)

    class Meta:
        model = Product
        fields = ['name', 'image', 'variants']
   
    def create(self,validated_data):
         variants_data=validated_data.pop('variants',[])
         product=Product.objects.create(**validated_data)
         for variant_data in variants_data:
            ProductVariant.objects.create(product=product, **variant_data)
         return product
        
class ProductBulkCreateSerializer(serializers.ListSerializer):
   
    def create(self, validated_data):
        variants_data = [item.pop('variants') for item in validated_data]

        products = [Product(**item) for item in validated_data]
        batch_size=calculate_batch_size(len(products)) 
        products = Product.objects.bulk_create(products,batch_size=batch_size)
        
        product_variants = []
        for product, variants in zip(products, variants_data):
            for variant_data in variants:
                product_variants.append(ProductVariant(product=product, **variant_data))
        
        ProductVariant.objects.bulk_create(product_variants,batch_size=10)
        
        return products  
        
    def validate(self, attrs):
          max_products = getattr(settings,'MAX_PRODUCTS')
          if len(attrs) > max_products:
              raise serializers.ValidationError("Exceeded maximum number {max_products} of products in bulk request")
          return attrs
         
    
class BulkProductSerializer(serializers.ModelSerializer):
    variants = ProductVariantSerializer(many=True)

    class Meta:
        model = Product
        fields = ['name', 'image', 'variants']
        list_serializer_class = ProductBulkCreateSerializer

