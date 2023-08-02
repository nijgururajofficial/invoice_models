from django.shortcuts import render, redirect, get_object_or_404
from django.forms import inlineformset_factory
from rest_framework import viewsets
from .models import Invoice, InvoiceDetail
from .serializers import InvoiceSerializer
from .forms import InvoiceForm, InvoiceDetailForm

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


def invoice_create(request):
    InvoiceDetailFormSet = inlineformset_factory(Invoice, InvoiceDetail, form=InvoiceDetailForm, extra=1)

    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        formset = InvoiceDetailFormSet(request.POST)

        if form.is_valid() and formset.is_valid():
            invoice = form.save()
            instances = formset.save()
            for instance in instances:
                instance.invoice = invoice
                instance.save()
            return redirect('invoice_list.html')
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
    invoice_details = invoice.details.all()
    context = {
        'invoice' : invoice,
        'invoice_details' : invoice_details
    }
    return render(request, 'invoice_detail.html', context)

def delete_invoice(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)
    invoice.delete()
    return redirect('invoice_list')