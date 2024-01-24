from django import forms

from hw3.models import Product


class EditProductForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all())
    title = forms.CharField()
    description = forms.CharField()
    price = forms.DecimalField()
    count = forms.IntegerField()


class AddImageProduct(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all())
    image = forms.ImageField()
