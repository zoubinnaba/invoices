from django import forms
from .models import ProductCategory, Product
from client.models import Client


class ProductCategoryForm(forms.ModelForm):
    name = forms.CharField(
        label="Category Name",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
            'placeholder': 'Enter category name'
        })
    )

    class Meta:
        model = ProductCategory
        fields = ['name']


class ProductForm(forms.ModelForm):
    name = forms.CharField(
        label="Product Name",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
            'placeholder': 'Enter product name'
        })
    )

    brand = forms.CharField(
        label="Brand",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
            'placeholder': 'Enter brand'
        })
    )

    reference = forms.CharField(
        label="Reference",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
            'placeholder': 'Enter reference'
        })
    )

    description = forms.CharField(
        label="Description",
        widget=forms.Textarea(attrs={
            'class': 'shadow appearance-none border h[40px] rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
            'placeholder': 'Enter description'
        })
    )

    price = forms.DecimalField(
        label="Price",
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={
            'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
            'placeholder': 'Enter price'
        })
    )

    tva = forms.DecimalField(
        label="TVA",
        max_digits=4,
        decimal_places=2,
        widget=forms.NumberInput(attrs={
            'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
            'placeholder': 'Enter TVA'
        })
    )

    category = forms.ModelChoiceField(
        queryset=ProductCategory.objects.all(),
        label="Category",
        widget=forms.Select(attrs={
            'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
        })
    )

    class Meta:
        model = Product
        fields = ['category', 'name', 'brand', 'reference', 'description', 'price', 'tva']
