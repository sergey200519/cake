from django.shortcuts import render
from django.template import RequestContext


from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.urls import reverse


from authapp.forms import UserLoginForm, UserRegisterForm
from mainapp.models import ProductCategories, Products, ImgProducts, SwiperSlides
from authapp.models import User

from django.db.models import Q

import json

# Create your views here.
def login(request):
    
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            pass
        else:
            print(form.errors)
    else:
        form = UserLoginForm()

    username = request.POST.get("username")
    password = request.POST.get("password")
    print(f"form is valid {username} and password is {password} ------------------->")
    # user = auth.authenticate(request, phone=username)
    try:
       user = User.objects.get(
                 Q(email=username) | Q(phone=username)
             )
    except:
        user = None
    print(user)
    if user is not None:
        pwd_valid = user.check_password(password)
        print(user, pwd_valid)
        if pwd_valid and user.is_active:
            auth.login(request, user)
    return HttpResponseRedirect(reverse("mainapp:index"))


    

def register(request):
    errors_flag = False
    popup = "null"
    if request.method == "POST":
        print("post --------------------------------------->")
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
                print("valid                 --------------------------------------->")
                form.save()
                popup = "'login'"
        else:
            popup = "'reg'"
            messages.set_level(request, messages.ERROR)
            messages.error(request, form.errors)
            print(form.errors, "------------------->errors")

        

    login_form = UserLoginForm()
    register_form = form

    context = {
        "title": "Главная",
        "swiper_slides": SwiperSlides.objects.all(),
        "product_categories": ProductCategories.objects.all(),
        "products": Products.objects.all(),
        "img_products": ImgProducts.objects.all(),
        "login_form": login_form,
        "register_form": register_form,
        "popup": popup
    }

    return render(request, "mainapp/index.html", context=context)

    return HttpResponseRedirect(reverse("mainapp:index"))

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("mainapp:index"))