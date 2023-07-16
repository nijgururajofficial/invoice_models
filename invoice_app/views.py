from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from .models import Invoice
from .serializers import InvoiceSerializer
from .forms import InvoiceForm, InvoiceDetailFormSet

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

def invoice_create(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        formset = InvoiceDetailFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            invoice = form.save()
            formset.instance = invoice
            formset.save()
            return redirect('invoice_list')
    else:
        form = InvoiceForm()
        formset = InvoiceDetailFormSet()

    context = {
        'form': form,
        'formset': formset,
    }
    return render(request, 'invoice_create.html', context)

def invoice_list(request):
    invoices = Invoice.objects.all()
    form = InvoiceForm()

    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('invoice_list')

    context = {
        'invoices': invoices,
        'form': form,
    }
    return render(request, 'invoice_list.html', context)

def invoice_detail(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)
    return render(request, 'invoice_detail.html', {'invoice': invoice})
