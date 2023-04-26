from django.shortcuts import render
from brand.models import Product,PImage

def get_product(request , slug):
    try:

        product = Product.objects.get(slug=slug)
        FImage = PImage.objects.filter(Product=product).first
        productsImages = PImage.objects.filter(Product=product)
        print(productsImages)
        context = {'product' : product,'FeaturedImage':FImage,'images':productsImages}

        return render(request, 'product/product.html' , context = context)
    except Exception as e:
        print(e)


# def get_all_products(request):
#     allproducts = Product.objects.all();
#     context = {
#         'AllProducts': allproducts
#     }
#     return  render(request,'product/product.html',context)