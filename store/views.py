from django.shortcuts import render, redirect
from .models import Products
from .forms import ProductForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import json
import traceback
import google.generativeai as genai




def product_list(request, tag_slug=None):
    products = Products.objects.all()  # Fetch all products
    tag = None

    if tag_slug:
        tag = request.GET.get('name')  # Get the tag name from the URL
        products = products.filter(tags__icontains=tag)  # Filter products by tag if provided


    return render(request, 'store/product_list.html', {'products': products, 'tag': tag})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            # Split comma-separated tags into a list
            tags = form.cleaned_data['tags'].split(',') if form.cleaned_data['tags'] else []
            tags = [tag.strip() for tag in tags]  # Clean whitespace
            # Manually create a Product instance and save to the database
            product = Products(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                price=form.cleaned_data['price'],
                category=form.cleaned_data['category'],
                tags=tags
            )
            product.save()  # Save the instance to MongoDB
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'store/add_product.html', {'form': form})

@csrf_exempt
def generate_tags(request):
    if request.method == 'POST':
        genai.configure(api_key=settings.GEMINI_KEY)
        model = genai.GenerativeModel('gemini-2.0-flash-lite')


        data = json.loads(request.body)
        name = data.get('name', '')
        description = data.get('description', '')
        category = data.get('category', '')

        prompt = f"You are a helpful assistant that will generate the corresponding tags from the given context. Do not return any explanation, just the string that contains the tags that are comma-separated. Generate SEO-friendly product tags (comma-separated) for a product with the following:\nName: {name}\nDescription: {description}\nCategory: {category}\n\nTags:"

        # Call Gemini API to generate tags
        try:
            bot_response = model.generate_content(prompt)
            tags = bot_response.text.strip()
            print(f"Generated tags: {tags}")  # Debugging line
            return JsonResponse({'tags': tags})
        except Exception as e:
            print(traceback.format_exc())
            return JsonResponse({'error': str(e)}, status=500)
