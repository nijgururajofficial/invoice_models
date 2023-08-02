from django import forms
from django.forms import inlineformset_factory
from .models import Invoice, InvoiceDetail

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['date', 'invoice_no', 'customer_name']

class InvoiceDetailForm(forms.ModelForm):
    class Meta:
        model = InvoiceDetail
        fields = ['invoice_no', 'description', 'quantity', 'unit_price', 'price']