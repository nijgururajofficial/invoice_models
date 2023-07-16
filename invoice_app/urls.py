from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InvoiceViewSet, invoice_list, invoice_create, invoice_detail

router = DefaultRouter()
router.register(r'invoices', InvoiceViewSet)

urlpatterns = [
    path('invoices/', invoice_list, name='invoice_list'),
    path('api/', include(router.urls)),
    path('invoices/create/', invoice_create, name='invoice_create'),
    path('invoices/<int:invoice_id>/', invoice_detail, name='invoice_detail'),
]