from django.shortcuts import render
from django.http import HttpResponse

# Model Imports
from .models import Product

# Form Imports
from .forms import ProductForm, RawProductForm

# Create your views here.
def home_view(request, *args, **kwargs):
    """ obj = Product.objects.get(id=1)
    context = {
        'title' : obj.title,
        'img' : obj.imagePreview
    } """
    query_results = Product.objects.all()
    context = {
        'products' : query_results
    }

    return render(request, "store/main.html", context)

def about_view(request, *args, **kwargs):
    """ my_context = {
        "my_text": "This is about us",
        "my_number": 123,
        "my_list": [123, 321, 921]
    } """
    return render(request, "store/about.html", {})

def product_detail_view(request):
    obj = Product.objects.get(id=2)
    """ context = {
        'title': obj.title,
        'description': obj.description
    } """
    context = {
        "object": obj
        }
    return render(request, "store/detail.html", context)

""" def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        "form": form
        }
    return render(request, "store/create.html", context) """

def product_create_view(request):
    form = RawProductForm()
    if request.method == "POST":
        form = RawProductForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            Product.objects.create(**form.cleaned_data)
        else:
            print(form.errors)
    context = {
        'form': form
    }
    return render(request, "store/create.html", context)