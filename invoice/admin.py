from django.contrib import admin

from invoice.models import Invoice, InvoiceItem

admin.site.register(Invoice)
admin.site.register(InvoiceItem)
