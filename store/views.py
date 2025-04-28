from django.shortcuts import render, redirect
from .models import Products
from .forms import ProductForm

def product_list(request):
    products = Products.objects.all()  # Fetch all products
    return render(request, 'store/product_list.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            # Manually create a Product instance and save to the database
            product = Products(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                price=form.cleaned_data['price'],
                category=form.cleaned_data['category']
            )
            product.save()  # Save the instance to MongoDB
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'store/add_product.html', {'form': form})

# Create your views here.
