from django import forms
from .models import Client


class ClientForm(forms.ModelForm):
    GENDER_CHOICES = [
        ('Mr.', 'Mister'),
        ('Ms.', 'Miss')
    ]

    first_name = forms.CharField(
        label="First Name",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
            'placeholder': 'Enter your first name'
        })
    )

    last_name = forms.CharField(
        label="Last Name",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
            'placeholder': 'Enter your last name'
        })
    )

    gender = forms.ChoiceField(
        label="Gender",
        choices=GENDER_CHOICES,
        widget=forms.RadioSelect(attrs={
            'class': 'form-radio h-4 w-4 text-blue-600',
        })
    )

    address = forms.CharField(
        label="Address",
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
            'placeholder': 'Enter your address'
        })
    )

    postal_code = forms.CharField(
        label="Postal Code",
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
            'placeholder': 'Enter your postal code'
        })
    )

    city = forms.CharField(
        label="City",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
            'placeholder': 'Enter your city'
        })
    )

    email = forms.EmailField(
        label="Email",
        max_length=254,
        widget=forms.TextInput(attrs={
            'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
            'placeholder': 'Enter your email'
        })
    )

    phone = forms.CharField(
        label="Phone Number",
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
            'placeholder': 'Enter your phone number'
        })
    )

    class Meta:
        model = Client
        fields = ['gender', 'first_name', 'last_name', 'address', 'postal_code', 'city', 'email', 'phone']
