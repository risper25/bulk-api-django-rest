from django.shortcuts import render
from rest_framework import status,generics
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product, ProductVariant
from .serializers import ProductSerializer, ProductVariantSerializer,BulkProductSerializer
import time
from memory_profiler import profile

# Create your views here.
class ProductListAPIView(APIView):
    def get(self,request: Request):
        products=Product.objects.all()
        serializer=ProductSerializer(instance=products,many=True)
        response={
            "message":"here are all the products",
            "data":serializer.data
        }
        return Response(data=response,status=status.HTTP_200_OK)
  
    def post(self,request : Request):
        product=request.data
        serializer=ProductSerializer(data=product,many=True)

        if serializer.is_valid():
            serializer.save()
            response={
                "message":"product saved succesfully",
                "data":serializer.data
            }
            return Response(data=response,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class BulkProductListAPIView(APIView):
    def get(self,request: Request):
        products=Product.objects.all()
        serializer=BulkProductSerializer(instance=products,many=True)
        response={
            "message":"here are all the products",
            "data":serializer.data
        }
        return Response(data=response,status=status.HTTP_200_OK)
  
    def post(self,request : Request):
        product=request.data
        serializer=BulkProductSerializer(data=product,many=True)

        if serializer.is_valid():
            serializer.save()
            response={
                "message":"product saved succesfully",
                "data":serializer.data
            }
            return Response(data=response,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
