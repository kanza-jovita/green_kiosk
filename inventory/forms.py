from django import forms
from .models import Product

class ProductuploadForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"