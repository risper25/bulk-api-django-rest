import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.test import TestCase
from .utils import generate_product_data
from inventory.models import Product,ProductVariant
from memory_profiler import profile
import time

class TestViews(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.test_data=generate_product_data(1000,save=True)
    def tearDown(self):
        # Clean up test data after each test method
        Product.objects.all().delete()    
        ProductVariant.objects.all().delete()    
    
    #@profile
    def test_bulk_add_products_and_variants_10(self):
        
        data=self.test_data[:10]
        url = reverse('products')
        start_time = time.time()
        response = self.client.post(url, data, format='json')
        execution_time = time.time() - start_time
        print("Execution time for 10 products:", execution_time, "seconds")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #@profile
    def test_bulk_add_products_and_variants_500(self):
        data=self.test_data[:500]
        url = reverse('products')
        start_time = time.time()
        response = self.client.post(url, data, format='json')
        execution_time = time.time() - start_time
        print("Execution time for 500 products:", execution_time, "seconds")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED) 

    #@profile
    def test_bulk_add_products_and_variants_1000(self):
        data=self.test_data[:1000]
        url = reverse('products')
        start_time = time.time()
        response = self.client.post(url, data, format='json')
        execution_time = time.time() - start_time
        print("Execution time for 1000 products:", execution_time, "seconds")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)      
        


