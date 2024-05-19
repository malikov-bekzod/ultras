from django import forms
from django.forms import inlineformset_factory
from .models import Product, ProductImage


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


ProductImageFormSet = inlineformset_factory(
    Product, ProductImage, fields=("image",), extra=4, max_num=4
)
