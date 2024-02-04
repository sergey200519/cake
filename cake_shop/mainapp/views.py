from django.shortcuts import render
from django.views.generic import DetailView, UpdateView
from mainapp.models import ProductCategories, SwiperSlides, Reviews, \
    ExclusiveCategories, ExclusiveProducts, ImgExclusive, \
    Product, ImgProduct

from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from authapp.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from mainapp.forms import ReviewsForm
from adminapp.forms import ApplicationsForm

# Create your views here.
def index(request):
    context = {
        "title": "Главная",
        "swiper_slides": SwiperSlides.objects.all(),
        "product_categories": ProductCategories.objects.all(),
        "products": Product.objects.all(),
        "img_products": ImgProduct.objects.all(),
        "popup": "null"
    }
    return render(request, "mainapp/index.html", context=context)


class ProductDetail(DetailView):
    model = Product
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


        context["title"] = context["product"].name
        context["img_products"] = ImgProduct.objects.filter(product=self.kwargs["pk"])
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
            product = Product.objects.get(id=pk)
            Reviews.objects.create(status="notactive", rating=form.data["rating"], 
                                   text=form.data["text"], product=product, author=request.user)
        else:
            print(form.errors, "------------------->errors")
    return  HttpResponseRedirect(reverse("mainapp:detail", args=(pk,)))

def exclusive(request):
    context = {
        "title": "Эксклюзивы",
        "swiper_slides": SwiperSlides.objects.all(),
        "exclusive_categories": ExclusiveCategories.objects.all(),
        "exclusives": ExclusiveProducts.objects.all(),
        "img_exclusives": ImgExclusive.objects.all(),
    }
    return  render(request,'mainapp/exclusive.html', context=context)


class ExclusiveDetail(DetailView):
    model = ExclusiveProducts
    template_name = "mainapp/detail_ex.html"
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["products"] = context["object"]
        context["title"] = context["products"].name
        context["img_products"] = ImgExclusive.objects.filter(exclusive=self.kwargs["pk"])
        return context
    


def application_add(request):
    if request.method == "POST":
        form = ApplicationsForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
        

def about_us(request):
    context = {
        "title": "Обо мне"
    }
    return render(request, "mainapp/about_us.html", context=context)

def partners(request):
    context = {
        "title": "Партнёры"
    }
    return render(request, "mainapp/partners.html", context=context)

def videos(request):
    context = {
        "title": "Видеоролики"
    }
    return render(request, "mainapp/videos.html", context=context)

def contacts(request):
    context = {
        "title": "Контакты"
    }
    return render(request, "mainapp/contacts.html", context=context)

def offer(request):
    context = {
        "title": "Оферта"
    }
    return render(request, "mainapp/offer.html", context=context)

def personalization(request):
    context = {
        "title": "Соглашение на обработку персональных данных"
    }
    return render(request, "mainapp/personalization.html", context=context)

def requisites(request):
    context = {
        "title": "Реквизиты"
    }
    return render(request, "mainapp/requisites.html", context=context)