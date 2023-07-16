from rest_framework import serializers
from .models import Invoice, InvoiceDetail

class InvoiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetail
        fields = ['id', 'description', 'quantity', 'unit_price', 'price']

class InvoiceSerializer(serializers.ModelSerializer):
    invoice_detail = InvoiceDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Invoice
        fields = ['id', 'date', 'invoice_no', 'customer_name', 'invoice_detail']

class InvoiceCreateSerializer(serializers.ModelSerializer):
    invoice_detail = InvoiceDetailSerializer(many=True)

    class Meta:
        model = Invoice
        fields = ['date', 'invoice_no', 'customer_name', 'invoice_detail']

    def create(self, validated_data):
        invoice_details_data = validated_data.pop('invoice_detail')
        invoice = Invoice.objects.create(**validated_data)
        invoice_details = []
        for detail_data in invoice_details_data:
            detail_data['invoice'] = invoice
            invoice_details.append(InvoiceDetail(**detail_data))
        InvoiceDetail.objects.bulk_create(invoice_details)
        return invoice
