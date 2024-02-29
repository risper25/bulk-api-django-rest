import logging
from django.shortcuts import render
from rest_framework import status,generics
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product, ProductVariant
from .serializers import ProductSerializer, ProductVariantSerializer,BulkProductSerializer
import time
from memory_profiler import profile
from rest_framework.pagination import PageNumberPagination



# Create your views here.
logger = logging.getLogger(__name__)
class ProductListAPIView(APIView,PageNumberPagination):
    def get(self,request: Request):
        
        products=Product.objects.all()
        products=self.paginate_queryset(products,request,view=self)
        serializer=ProductSerializer(products,many=True)
        
        return self.get_paginated_response(serializer.data)
  
    def post(self,request : Request):
        try:
            product=request.data
            serializer=ProductSerializer(data=product,many=isinstance(product, list))

            if serializer.is_valid():
                serializer.save()
                response={
                    "message":"products saved succesfully",
                    "data":serializer.data
                }
                return Response(data=response,status=status.HTTP_201_CREATED)
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            error_message = str(e)
            logger.error(error_message)
            return Response(data={"message": "database  error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class BulkProductListAPIView(APIView,PageNumberPagination):
    def get(self,request: Request):
        products=Product.objects.all()
        products=self.paginate_queryset(products,request,view=self)
        serializer=BulkProductSerializer(instance=products,many=True)
        return self.get_paginated_response(serializer.data)
        
  
    def post(self,request : Request):
        try:
            product=request.data
            serializer=BulkProductSerializer(data=product,many=True)

            if serializer.is_valid():
                serializer.save()
                response={
                    "message":"products saved succesfully",
                    "data":serializer.data
                }
                return Response(data=response,status=status.HTTP_201_CREATED)
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            error_message = str(e)
            logger.error(error_message)
            return Response(data={"message": "database  error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    
