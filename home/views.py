from django.shortcuts import render
# from products.models import Product
from brand.models import Product ,PImage


def index(request):

    allproducts = Product.objects.all()
    print(allproducts)
    for product in allproducts:
        ProductImage = PImage.objects.filter(Product=product).first
        print(ProductImage)
    context = {'products' : allproducts,'PImage':ProductImage}
    return render(request , 'home/index.html' , context)