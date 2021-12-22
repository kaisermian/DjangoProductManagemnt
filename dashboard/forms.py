from django.forms import ModelForm
from dashboard.models import Product
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit 

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'price', 'category')