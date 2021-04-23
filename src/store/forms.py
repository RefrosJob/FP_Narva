from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'descriptionShort',
            'price',
            'imagePreview',
            'imageMain'      
        ]

class RawProductForm(forms.Form):
    # Text Forms
    title             = forms.CharField(widget = forms.Textarea)
    description       = forms.CharField(widget = forms.Textarea)
    descriptionShort  = forms.CharField(
        label = 'Short Description', 
        widget = forms.Textarea(
            attrs={
                'class': 'new-class-name second-class-name',
                'rows': 5
            }
        )
    )

    # Decimal Forms
    price             = forms.DecimalField(initial = 1.00)

    # Image Forms

    imagePreview      = forms.ImageField()
    imageMain         = forms.ImageField()
    
