from django.shortcuts import render

# Create your views here.

def indexpage(request):
    return render(request, 'mainapp/index.html')    # в пространстве имен mainapp

def products(request):
    return render(request, 'mainapp/products.html')

def contact(request):
    return render(request, 'mainapp/contact.html')
