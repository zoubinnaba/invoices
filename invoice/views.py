from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404

from product.models import Product
from .forms import InvoiceForm, InvoiceItemForm
from .models import Invoice, InvoiceItem
from django.http import HttpResponse, JsonResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


@login_required
def create_invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        category_id = request.POST.get('category')
        if category_id:
            form.fields['product'].queryset = Product.objects.filter(category_id=category_id)

        if form.is_valid():
            form.save()
            return redirect('invoice:list_invoice')
        else:
            print(form.errors)
    else:
        form = InvoiceForm()
        form.fields['product'].queryset = Product.objects.none()

    return render(request, 'invoice/create_invoice.html', {'form': form})


@login_required
def list_invoice(request):
    invoice_list = Invoice.objects.all().order_by('-date')
    paginator = Paginator(invoice_list, 6)

    page_number = request.GET.get('page')
    invoices = paginator.get_page(page_number)
    return render(request, 'invoice/list_invoice.html', {'invoices': invoices})


@login_required
def get_products_by_category(request, category_id):
    products = Product.objects.filter(category_id=category_id).values('id', 'name')
    return JsonResponse(list(products), safe=False)


@login_required
def add_invoice_item(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)
    if request.method == 'POST':
        form = InvoiceItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.invoice = invoice
            item.save()
            return redirect('invoice:add_invoice_item', invoice_id=invoice.id)
        else:
            form_errors = form.errors
    else:
        form = InvoiceItemForm()
        form_errors = None

    return render(request, 'invoice/add_invoice_item.html', {
        'form': form,
        'invoice': invoice,
        'form_errors': form_errors,
    })


@login_required
def delete_invoice_item(request, item_id):
    item = get_object_or_404(InvoiceItem, id=item_id)
    invoice_id = item.invoice.id
    item.delete()
    return redirect('invoice:add_invoice_item', invoice_id=invoice_id)


@login_required
def generate_invoice_pdf(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)
    template_path = 'invoice/invoice_pdf.html'
    context = {'invoice': invoice}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="invoice_{invoice.id}.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
