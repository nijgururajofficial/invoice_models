from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'invoices', views.InvoiceViewSet)

urlpatterns = [
    path('', views.invoice_list, name='invoice_list'),
    path('api/', include(router.urls)),
    path('invoices/create/', views.invoice_create, name='invoice_create'),
    path('invoices/<int:invoice_id>/', views.invoice_detail, name='invoice_detail'),
    path('delete_invoice/<int:invoice_id>/', views.delete_invoice, name='delete_invoice'),
]