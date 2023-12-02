from django.shortcuts import render
from django.views.generic import DetailView
from mainapp.models import ProductCategories, Products, ImgProducts, SwiperSlides, Reviews

from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse

from authapp.forms import UserLoginForm, UserRegisterForm
from mainapp.forms import ReviewsForm

# Create your views here.
def index(request):
    context = {
        "title": "Главная",
        "swiper_slides": SwiperSlides.objects.all(),
        "product_categories": ProductCategories.objects.all(),
        "products": Products.objects.filter(exclusive="notexclusive"),
        "img_products": ImgProducts.objects.all(),
        "popup": "null"
    }
    return  render(request,'mainapp/index.html', context=context)


class ProductDetail(DetailView):
    model = Products
    template_name = "mainapp/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        add_review = True
        for item in Reviews.objects.filter(product=self.kwargs["pk"], status="active"):
            if item.author == self.request.user:
                add_review = False
                break
        if not self.request.user.is_authenticated:
            add_review = False


        context["title"] = context["products"].name
        context["img_products"] = ImgProducts.objects.filter(product=self.kwargs["pk"])
        context["reviews"] = Reviews.objects.filter(product=self.kwargs["pk"])
        context["review_form"] = ReviewsForm()
        context["add_review"] = add_review
        return context


def add_review(request, pk):
    if request.method == "POST":
        form = ReviewsForm(data=request.POST)
        if form.is_valid():
            # flag = True
            # for item in Reviews.objects.all():
            #     if item.author == request.user:
            #         flag = False
            #         break
            product = Products.objects.get(id=pk)
            Reviews.objects.create(status="notactive", rating=form.data["rating"], 
                                   text=form.data["text"], product=product, author=request.user)
        else:
            print(form.errors, "------------------->errors")
    return  HttpResponseRedirect(reverse("mainapp:detail", args=(pk,)))