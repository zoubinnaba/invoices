from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django import forms
from .models import UserProfile


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label="Email", max_length=254,
                             widget=forms.TextInput(attrs={
                                 'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
                                 'placeholder': 'Enter your email'}))
    password1 = forms.CharField(label="Password",
                                widget=forms.PasswordInput(attrs={
                                    'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
                                    'placeholder': 'Enter your password'}))
    password2 = forms.CharField(label="Confirm Password",
                                widget=forms.PasswordInput(attrs={
                                    'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
                                    'placeholder': 'Confirm your password'}))

    class Meta:
        model = UserProfile
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):
    email = forms.EmailField(label="Email", max_length=254,
                             widget=forms.TextInput(attrs={
                                 'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
                                 'placeholder': 'Enter your email'}))
    password1 = forms.CharField(label="Password",
                                widget=forms.PasswordInput(attrs={
                                    'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
                                    'placeholder': 'Enter your password'}))
    password2 = forms.CharField(label="Confirm Password",
                                widget=forms.PasswordInput(attrs={
                                    'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
                                    'placeholder': 'Confirm your password'}))

    class Meta:
        model = UserProfile
        fields = ("email",)


class LoginForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=254,
                             widget=forms.TextInput(attrs={
                                 'class': 'mt-4 shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
                                 'placeholder': 'Enter your email'}))
    password = forms.CharField(label="Password",
                               widget=forms.PasswordInput(attrs={
                                   'class': 'mt-4 shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
                                   'placeholder': 'Enter your password'}))