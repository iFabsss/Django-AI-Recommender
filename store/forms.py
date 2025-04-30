from django import forms

class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.FloatField()
    category = forms.CharField(max_length=50)
    tags = forms.CharField(max_length=1000, required=False)  # Optional field for tags
    