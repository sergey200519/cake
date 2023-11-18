from django.shortcuts import render
from django.views.generic import DetailView
from mainapp.models import ProductCategories, Products, ImgProducts, SwiperSlides

from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    # if request.method == "POST":
    #     login_form = UserLoginForm(data=request.POST)
    #     if login_form.is_valid():
    #         username = request.POST.get("username")
    #         password = request.POST.get("password")
    #         user = auth.authenticate(username=username, password=password)
    #         if user.is_active:
    #             auth.login(request, user)
    #             return HttpResponseRedirect(reverse("mainapp:index"))
    #     else:
    #         print(form.errors)
    # else:
    # login_form = UserLoginForm()


    # context = {
    #     "title": "Вход",
    #     "form": form
    # }
    context = {
        "title": "Главная",
        "swiper_slides": SwiperSlides.objects.all(),
        "product_categories": ProductCategories.objects.all(),
        "products": Products.objects.all(),
        "img_products": ImgProducts.objects.all(),
        # "login_form": login_form
    }
    return  render(request,'mainapp/index.html', context=context)


class ProductDetail(DetailView):
    model = Products
    template_name = "mainapp/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = context["products"].name
        context["img_products"] = ImgProducts.objects.filter(product=self.kwargs["pk"])
        return context