from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import ListView, TemplateView, CreateView, DeleteView, UpdateView, DetailView

from mainapp.models import ProductCategories, Reviews, SwiperSlides, Product, ImgProduct, BaseProduct
from mainapp.mixin import CustomDispatchMixin

from authapp.models import User

from adminapp.forms import CreateProductForm, UploadFileForm, CategoryCreateForm, SlidesForm, PromoForm
from adminapp.models import Applications

from orderapp.models import Order, PromoCode

import json

# Create your views here.
class IndexTemplateView(TemplateView, CustomDispatchMixin):
    template_name = "adminapp/admin.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Главня страница aдминки"
        context["count_new_orders"] = Order.get_count_new_orders()
        context["count_new_reviews"] = Reviews.get_count_new_reviews()
        context["count_new_applications"] = Applications.get_count_new_applications()
        return context
    

class ProductsListView(ListView, CustomDispatchMixin):
    model = Product
    template_name = "adminapp/products_admin.html"
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        products_json = []
        for item in BaseProduct.objects.all():
            products_json.append(item.article)

        context["title"] = "Админка | Товары"
        context["data"] = json.dumps(products_json)
        context["form"] = CreateProductForm()
        context["formset"] = UploadFileForm()
        return context
    
@user_passes_test(lambda u: u.is_superuser)
def admin_product_create(request):
    if request.method == "POST":
        form = CreateProductForm(request.POST, request.FILES)
        formset = UploadFileForm(request.POST, request.FILES)
        
        if form.is_valid():
            data = form.data
            name = data["name"]
            ingredients = data["ingredients"]
            description = data["description"]
            category = ProductCategories.objects.get(id=data["category"])

            article_four_hundred = data["article_four_hundred"]
            price_four_hundred = data["price_four_hundred"]

            article_six_hundred = data["article_six_hundred"]
            price_six_hundred = data["price_six_hundred"]

            article_eight_hundred = data["article_eight_hundred"]
            price_eight_hundred = data["price_eight_hundred"]

            article_one_thousand = data["article_one_thousand"]
            price_one_thousand = data["price_one_thousand"]

            article_two_thousand = data["article_two_thousand"]
            price_two_thousand = data["price_two_thousand"]

            base_product_400 = BaseProduct.objects.create(article=article_four_hundred, \
                                                      weight=400, \
                                                      price=price_four_hundred)
            base_product_600 = BaseProduct.objects.create(article=article_six_hundred, \
                                                      weight=600, \
                                                      price=price_six_hundred)
            base_product_800 = BaseProduct.objects.create(article=article_eight_hundred, \
                                                      weight=800, \
                                                      price=price_eight_hundred)
            base_product_1000 = BaseProduct.objects.create(article=article_one_thousand, \
                                                       weight=1000, \
                                                       price=price_one_thousand)
            base_product_2000 = BaseProduct.objects.create(article=article_two_thousand, \
                                                       weight=2000, \
                                                       price=price_two_thousand)
            base_products = (base_product_400, base_product_600, base_product_800, base_product_1000, base_product_2000)
            
            new_product = Product.objects.create(name=name, \
                                                 ingredients=ingredients, \
                                                 description=description, \
                                                 category=category)
            for product in base_products:
                new_product.products.add(product)

            # new_product = Products.objects.create(name=name, ingredients=ingredients, description=description, category=category, \
            #     article_four_hundred=article_four_hundred, price_four_hundred=price_four_hundred, \
            #     article_six_hundred=article_six_hundred, price_six_hundred=price_six_hundred, \
            #     article_eight_hundred=article_eight_hundred, price_eight_hundred=price_eight_hundred, \
            #     article_one_thousand=article_one_thousand, price_one_thousand=price_one_thousand, \
            #     article_two_thousand=article_two_thousand, price_two_thousand=price_two_thousand)

            for uploaded_file in request.FILES.getlist("files"):
                # print(f"test ---> {uploaded_file}")
                ImgProduct.objects.create(image=uploaded_file, product=new_product)
            
        else:
            print(form.errors)

    return HttpResponseRedirect(reverse("adminapp:products"))

@user_passes_test(lambda u: u.is_superuser)
def admin_product_remove(request, pk):
    Product.objects.get(id=pk).delete()
    return HttpResponseRedirect(reverse("adminapp:products"))

@user_passes_test(lambda u: u.is_superuser)
def admin_product_update(request, pk):
    product = Product.objects.get(id=pk)
    files = ImgProduct.objects.filter(product=pk)
    data = {
        "name": product.name,
        "ingredients": product.ingredients,
        "description": product.description,
        "category": (product.category.id, product.category.name),

        "article_four_hundred": product.products.get(weight=400).article,
        "price_four_hundred": product.products.get(weight=400).price,

        "article_six_hundred": product.products.get(weight=600).article,
        "price_six_hundred": product.products.get(weight=600).price,

        "article_eight_hundred": product.products.get(weight=800).article,
        "price_eight_hundred": product.products.get(weight=800).price,

        "article_one_thousand": product.products.get(weight=1000).article,
        "price_one_thousand": product.products.get(weight=1000).price,

        "article_two_thousand": product.products.get(weight=2000).article,
        "price_two_thousand": product.products.get(weight=2000).price
    }
    if request.method == "POST":
        
        form = CreateProductForm(request.POST, request.FILES)
        if form.is_valid():
            
            data = form.data
            name = data["name"]
            ingredients = data["ingredients"]
            description = data["description"]
            category = ProductCategories.objects.get(id=data["category"])

            article_four_hundred = data["article_four_hundred"]
            price_four_hundred = data["price_four_hundred"]

            article_six_hundred = data["article_six_hundred"]
            price_six_hundred = data["price_six_hundred"]

            article_eight_hundred = data["article_eight_hundred"]
            price_eight_hundred = data["price_eight_hundred"]

            article_one_thousand = data["article_one_thousand"]
            price_one_thousand = data["price_one_thousand"]

            article_two_thousand = data["article_two_thousand"]
            price_two_thousand = data["price_two_thousand"]

            base_product_400 = BaseProduct.objects.get(article=product.products.get(weight=400).article)
            base_product_400.article = article_four_hundred
            base_product_400.price = price_four_hundred
            base_product_400.save()

            base_product_600 = BaseProduct.objects.get(article=product.products.get(weight=600).article)
            base_product_600.article = article_six_hundred
            base_product_600.price = price_six_hundred
            base_product_600.save()
            
            base_product_800 = BaseProduct.objects.get(article=product.products.get(weight=800).article)
            base_product_800.article = article_eight_hundred
            base_product_800.price = price_eight_hundred
            base_product_800.save()

            base_product_1000 = BaseProduct.objects.get(article=product.products.get(weight=1000).article)
            base_product_1000.article = article_one_thousand
            base_product_1000.price = price_one_thousand
            base_product_1000.save()

            base_product_2000 = BaseProduct.objects.get(article=product.products.get(weight=2000).article)
            base_product_2000.article = article_two_thousand
            base_product_2000.price = price_two_thousand
            base_product_2000.save()
            

            product.name = name
            product.ingredients = ingredients
            product.description = description
            product.category = category
            product.save()

            for uploaded_file in request.FILES.getlist("files"):
                ImgProduct.objects.create(image=uploaded_file, product=product)
        else:
            print(form.errors)

    
    context = {
        "title": "Админка | Изменение",
        "form": CreateProductForm(data),
        "formset": UploadFileForm(),
        "files": files,
        "product": product
    }

    return render(request,"adminapp/product_update.html",context)

@user_passes_test(lambda u: u.is_superuser)
def admin_product_img_remove(request, pk, id):
    ImgProduct.objects.get(id=pk).delete()
    return HttpResponseRedirect(reverse("adminapp:product_update", args=[id]))







class CategoriesListView(ListView, CustomDispatchMixin):
    model = ProductCategories
    template_name = "adminapp/categories_admin.html"
    context_object_name = "product_categories"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Админка | Категории"
        context["form"] = CategoryCreateForm()
        return context
    
@user_passes_test(lambda u: u.is_superuser)
def creaate_categories(request):
    if request.method == "POST":
        form = CategoryCreateForm(request.POST)
        if form.is_valid():
            form.save()
    return HttpResponseRedirect(reverse("adminapp:categories"))

class CategoryUpdateView(UpdateView, CustomDispatchMixin):
    model = ProductCategories
    fields = ["name"]
    template_name = "adminapp/categories_update.html"
    success_url = reverse_lazy("adminapp:categories")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = {
            "name": context["object"].name
        }
        context["title"] = "Админка | Изменение категории"
        context["form"] = CategoryCreateForm(data)
        return context
    
    def post(self, request, **kwargs):
        form = CreateProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return super(CategoryUpdateView, self).post(request, **kwargs)


@user_passes_test(lambda u: u.is_superuser)
def admin_category_remove(request, pk):
    ProductCategories.objects.get(id=pk).delete()
    return HttpResponseRedirect(reverse("adminapp:categories"))



class UsersListView(ListView, CustomDispatchMixin):
    model = User
    template_name = "adminapp/users.html"
    context_object_name = "users"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Админка | Пользователи"
        return context

@user_passes_test(lambda u: u.is_superuser)
def admin_user_notactive(request, pk):
    user = User.objects.get(id=pk)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse("adminapp:users"))

@user_passes_test(lambda u: u.is_superuser)
def admin_user_active(request, pk):
    user = User.objects.get(id=pk)
    user.is_active = True
    user.save()
    return HttpResponseRedirect(reverse("adminapp:users"))



class ReviewsListView(ListView, CustomDispatchMixin):
    model = Reviews
    template_name = "adminapp/reviews.html"
    context_object_name = "reviews"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Админка | Отзывы"
        return context

@user_passes_test(lambda u: u.is_superuser)
def admin_review_approve(request, pk):
    review = Reviews.objects.get(id=pk)
    review.status = "active"
    review.new = False
    review.save()
    return HttpResponseRedirect(reverse("adminapp:reviews"))

@user_passes_test(lambda u: u.is_superuser)
def admin_review_cancel(request, pk):
    review = Reviews.objects.get(id=pk)
    review.status = "notactive"
    review.new = False
    review.save()
    return HttpResponseRedirect(reverse("adminapp:reviews"))

@user_passes_test(lambda u: u.is_superuser)
def admin_review_remove(request, pk):
    review = Reviews.objects.get(id=pk)
    product = review.product
    review.delete()
    product.recalculate_reviews()
    return HttpResponseRedirect(reverse("adminapp:reviews"))

class SlidesListView(ListView, CustomDispatchMixin):
    model = SwiperSlides
    template_name = "adminapp/slides.html"
    context_object_name = "slides"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Админка | Слайдер"
        context["form"] = SlidesForm()
        return context
    
    def post(self, request, **kwargs):
        form = SlidesForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse("adminapp:slides"))
    

class SlideUpdateView(UpdateView, CustomDispatchMixin):
    model = SwiperSlides
    fields = ["title", "description", "img"]
    template_name = "adminapp/slides_update.html"
    context_object_name = "slide"
    success_url = reverse_lazy("adminapp:slides")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = {
            "title": context["object"].title,
            "description": context["object"].description,
            "img": context["object"].img.url,
            # "slide": context["object"]
        }
        context["title"] = "Админка | Изменение слайд"
        context["form"] = SlidesForm(data)
        return context
    
    def post(self, request, **kwargs):
        instance = get_object_or_404(SwiperSlides, id=kwargs.get("pk"))
        form = SlidesForm(data=request.POST,files=request.FILES, instance=instance)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        return HttpResponseRedirect(reverse("adminapp:slides"))
    
@user_passes_test(lambda u: u.is_superuser)
def admin_slide_remove(request, pk):
    SwiperSlides.objects.get(id=pk).delete()
    return HttpResponseRedirect(reverse("adminapp:slides"))


class ApplicationsListView(ListView, CustomDispatchMixin):
    model = Applications
    template_name = "adminapp/support.html"
    context_object_name = "applications"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Админка | Потдержка"
        return context

@user_passes_test(lambda u: u.is_superuser)
def admin_application_read(request, pk):
    application = Applications.objects.get(id=pk)
    application.new = False
    application.save()
    return HttpResponseRedirect(reverse("adminapp:applications"))

@user_passes_test(lambda u: u.is_superuser)
def admin_application_remove(request, pk):
    Applications.objects.get(id=pk).delete()
    return HttpResponseRedirect(reverse("adminapp:applications"))


class OrdersListView(ListView, CustomDispatchMixin):
    model = Order
    template_name = "adminapp/orders_admin.html"
    context_object_name = "orders"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Админка | Заказы"
        context["orders"] = Order.objects.all().order_by("-id")
        return context
    
class PromoListView(ListView, CustomDispatchMixin):
    model = PromoCode
    template_name = "adminapp/promo_admin.html"
    context_object_name = "promocodes"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Админка | Промокоды"
        context["promo_form"] = PromoForm()
        return context
    
@user_passes_test(lambda u: u.is_superuser)
def admin_promo_create(request):
    if request.method == "POST":
        form = PromoForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
    return HttpResponseRedirect(reverse("adminapp:promo"))

class PromoUpdateView(UpdateView, CustomDispatchMixin):
    model = PromoCode
    fields = "__all__"
    template_name = "adminapp/promo_update.html"
    success_url = reverse_lazy("adminapp:promo")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = {
            "promo_code": context["object"].promo_code,
            "discount": context["object"].discount,
            "date": context["object"].date
        }
        context["title"] = "Админка | Изменение промоода"
        context["promo_form"] = PromoForm(data)
        context["promo"] = context["object"]
        return context
    
    def post(self, request, **kwargs):
        form = PromoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return super(PromoUpdateView, self).post(request, **kwargs)

@user_passes_test(lambda u: u.is_superuser)
def admin_promo_remove(request, pk):
    PromoCode.objects.get(id=pk).delete()
    return HttpResponseRedirect(reverse("adminapp:promo"))