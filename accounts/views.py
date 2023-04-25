from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.http import HttpResponseRedirect,HttpResponse
from pipenv.core import console
from .forms import *


from .models import Profile
from products.models import *
from accounts.models import Cart , CartItems


def login_page(request):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = email)

        if not user_obj.exists():
            messages.warning(request, 'Account not found.')
            return HttpResponseRedirect(request.path_info)


        # if not user_obj[0].profile.is_email_verified:
        #     messages.warning(request, 'Your account is not verified.')
        #     return HttpResponseRedirect(request.path_info)

        user_obj = authenticate(username = email , password= password)
        if user_obj:
            login(request , user_obj)
            return redirect('/')

        messages.warning(request, 'Invalid credentials')
        return HttpResponseRedirect(request.path_info)


    return render(request ,'accounts/login.html')


def register_page(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = email)

        if user_obj.exists():
            messages.warning(request, 'Email is already taken.')
            return HttpResponseRedirect(request.path_info)

        print(email)

        user_obj = User.objects.create(first_name = first_name , last_name= last_name , email = email , username = email)
        user_obj.set_password(password)
        user_obj.save()

        messages.success(request, 'An email has been sent on your mail.')
        return HttpResponseRedirect(request.path_info)


    return render(request ,'accounts/register.html')


def brand(request):
    return render(request,'accounts/brand_register.html')


def brand_login(request):
    return render(request,'accounts/brand_login.html')




# def brand_register(request):
#     if request.method == 'POST':
#         context = {}
#         # create object of form
#         form = BrandForm(request.POST or  None, request.FILES or None)
#
#         # check if form data is valid
#         if form.is_valid():
#             form.save()
#         context['form'] = form
#         return redirect('accounts/brand_login.html')
#     return render(request , 'accounts/brand_register.html')
#
#
# def brand_login(request):
#     if request.method=='POST':
#         brand_email = request.POST['brand_email']
#         brand_password = request.POST['brand_password']
#         brands = Brand.objects.filter(Brand_Email=brand_email,Brand_Password=brand_password)
#
#         if brands.exists():
#            for brand in brands:
#                BrandId = brand.id
#            response = redirect('brand_dashboard')
#            response.set_cookie('Brand_ID',BrandId)
#            return response
#         else:
#
#             messages.error(request,"Brand Credentials")
#             return render(request, 'brand_login.html')
#
#     return render(request,'brand_login.html')

# def brand_dashboard(request):
#
#     BrandId = request.COOKIES['Brand_ID']
#     brands = Brand.objects.filter(id=BrandId)
#
#     for brand in brands:
#         CBrand = Brand(Brand_Name=brand.Brand_Name, Brand_Email=brand.Brand_Email, Brand_Password=brand.Brand_Password,
#                        Brand_Address=brand.Brand_Address, Brand_City=brand.Brand_City, Brand_State=brand.Brand_State,
#                        Brand_Zip=brand.Brand_Zip, Brands_Logo=brand.Brands_Logo)
#
#
#     Brand_Products = Product.objects.filter(Product_Brand__Brand_Name__contains=CBrand.Brand_Name)
#     context = {
#         'BProducts': Brand_Products
#     }
#     return render (request,"brand_dashboard.html",context)


def activate_email(request , email_token):
    try:
        user = Profile.objects.get(email_token= email_token)
        user.is_email_verified = True
        user.save()
        return redirect('/')
    except Exception as e:
        return HttpResponse('Invalid Email token')



def add_to_cart(request,uid):
    variant = request.GET.get('variant')
    product = Product.objects.get(uid=uid)
    user = request.user
    cart, _  = Cart.objects.get_or_create(user=user,is_paid=False)
    cart_item = CartItems.objects.create(cart=cart,product=product)

    if variant:                                                                   #variant is not storing in cart_items
        variant = request.GET.get('variant')
        print(variant)
        console.log(variant)
        size_variant = SizeVariant.objects.get(size_name=variant)
        cart_item.size_variant = size_variant
        cart_item.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def cart(request):
    cart = Cart.objects.filter(is_paid=False, user=request.user).first()
    context = {'cart': cart}
    return render(request, 'accounts/cart.html',context)


def remove_cart(request, uid):
    try:
        cart_item = CartItems.objects.get(uid=uid)
        cart_item.delete()
    except Exception as e:
        print(e)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def signOut(request):
    logout(request)
    return redirect('login')
