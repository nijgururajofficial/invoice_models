from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Invoice

class InvoiceAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_invoice(self):
        url = reverse('invoice-list')
        data = {
            'date': '2023-07-14',
            'invoice_no': 'INV001',
            'customer_name': 'John Doe',
            'details': [
                {
                    'description': 'Product A',
                    'quantity': 2,
                    'unit_price': 10.0,
                    'price': 20.0
                },
                {
                    'description': 'Product B',
                    'quantity': 3,
                    'unit_price': 15.0,
                    'price': 45.0
                }
            ]
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Invoice.objects.count(), 1)
        self.assertEqual(Invoice.objects.first().invoice_no, 'INV001')
        self.assertEqual(Invoice.objects.first().customer_name, 'John Doe')
        self.assertEqual(Invoice.objects.first().details.count(), 2)
