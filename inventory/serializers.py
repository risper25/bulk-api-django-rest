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
        products = Product.objects.bulk_create(products)
        
        product_variants = []
        for product, variants in zip(products, variants_data):
            for variant_data in variants:
                product_variants.append(ProductVariant(product=product, **variant_data))
        batch_size=calculate_batch_size(len(products)) 
        ProductVariant.objects.bulk_create(product_variants,batch_size=batch_size)
        
        return products        
    
class BulkProductSerializer(serializers.ModelSerializer):
    variants = ProductVariantSerializer(many=True)

    class Meta:
        model = Product
        fields = ['name', 'image', 'variants']
        list_serializer_class = ProductBulkCreateSerializer

