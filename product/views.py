from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .forms import ProductCategoryForm, ProductForm
from django.contrib.auth.decorators import login_required

from .models import ProductCategory, Product


@login_required
def create_category(request):
    if request.method == 'POST':
        form = ProductCategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            return redirect('product:list_product')
    else:
        form = ProductCategoryForm()
    return render(request, 'product/create_category.html', {'form': form})


@login_required
def create_product(request):
    categories = ProductCategory.objects.filter(user=request.user)

    if request.method == 'POST':
        form = ProductForm(request.POST)
        form.fields['category'].queryset = categories

        if form.is_valid():
            form.save()
            return redirect('product:list_product')
        else:
            print(form.errors)
    else:
        form = ProductForm()
        form.fields['category'].queryset = categories

    return render(request, 'product/create_product.html', {'form': form})


@login_required
def list_product(request):
    product_list = Product.objects.all().order_by('name')
    paginator = Paginator(product_list, 4)

    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    return render(request, 'product/list_product.html', {'products': products})
