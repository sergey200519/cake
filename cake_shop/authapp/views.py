from django.shortcuts import render
from django.template import RequestContext
from django.views.generic import DetailView, UpdateView


from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy


from authapp.forms import UserLoginForm, UserRegisterForm
from mainapp.models import ProductCategories, Products, ImgProducts, SwiperSlides
from authapp.models import User, ImgUser

from django.db.models import Q

from authapp.forms import UserProfileForm

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

def profile_edit(request):
    print(request.method, "<--------------------------------", request.method == "POST")
    if request.method == "POST":
        form = UserProfileForm(data=request.POST,files=request.FILES,instance=request.user)
        print(form.is_valid())
        if form.is_valid():
            form.save()

        else:
            print(form.errors, "<-------------------------------- erros")
            print(form.data)
            
    context = {
        "title": "Главная",
        "swiper_slides": SwiperSlides.objects.all(),
        "product_categories": ProductCategories.objects.all(),
        "products": Products.objects.all(),
        "img_products": ImgProducts.objects.all(),
        "popup": "null"
    }

    return render(request, "mainapp/index.html", context=context)



# class ProfileFormView(UpdateView,BaseClassContextMixin,UserDispatchMixin):
#     # model = User
#     form_class = UserProfileForm
#     success_url = reverse_lazy('authapp:index')


#     def post(self, request, *args, **kwargs):
#         form =UserProfileForm(data=request.POST,files=request.FILES,instance=request.user)
#         profile_form = UserProfileEditForm(data=request.POST,files=request.FILES,instance=request.user.userprofile)
#         if form.is_valid() and profile_form.is_valid():
#             form.save()
#         return redirect(self.success_url)

#     def get_context_data(self, **kwargs):
#         context = super(ProfileFormView, self).get_context_data()
#         context['profile'] = UserProfileEditForm(instance=self.request.user.userprofile)
#         return context


#     def form_valid(self, form):
#         messages.set_level(self.request,messages.SUCCESS)
#         messages.success(self.request,'Вы успешно сохранили профиль')
#         super().form_valid(form)
#         return HttpResponseRedirect(self.get_success_url())

#     def get_object(self, queryset=None):
#         return User.objects.get(id=self.request.user.pk)