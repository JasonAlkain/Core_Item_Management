from django import forms
from django.forms import ModelForm
from .models import Item, Vendor


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'


class EditItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'count', 'category', 'price']


class VendorForm(ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'


class EditVendorForm(ModelForm):
    class Meta:
        model = Vendor
        fields = ['name', 'contact']

