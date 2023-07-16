from django import forms
from django.forms import inlineformset_factory
from .models import Invoice, InvoiceDetail

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['date', 'invoice_no', 'customer_name']

InvoiceDetailFormSet = inlineformset_factory(Invoice, InvoiceDetail, fields=['description', 'quantity', 'unit_price', 'price'], extra=1)
