from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import ListView, TemplateView, CreateView, DeleteView, UpdateView, DetailView

from mainapp.models import Products, ProductCategories, ImgProducts, Reviews
from mainapp.mixin import CustomDispatchMixin

from authapp.models import User

from adminapp.forms import CreateProductForm, UploadFileForm, CategoryCreateForm

import json

# Create your views here.
class IndexTemplateView(TemplateView, CustomDispatchMixin):
    template_name = "adminapp/admin.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Главня страница aдминки"
        return context
    

class ProductsListView(ListView, CustomDispatchMixin):
    model = Products
    template_name = "adminapp/products_admin.html"
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        products_json = []
        for item in Products.objects.all():
            products_json.append([item.article_four_hundred, item.article_six_hundred, item.article_eight_hundred, item.article_one_thousand, item.article_two_thousand])

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


            new_product = Products.objects.create(name=name, ingredients=ingredients, description=description, category=category, \
                article_four_hundred=article_four_hundred, price_four_hundred=price_four_hundred, \
                article_six_hundred=article_six_hundred, price_six_hundred=price_six_hundred, \
                article_eight_hundred=article_eight_hundred, price_eight_hundred=price_eight_hundred, \
                article_one_thousand=article_one_thousand, price_one_thousand=price_one_thousand, \
                article_two_thousand=article_two_thousand, price_two_thousand=price_two_thousand)

            for uploaded_file in request.FILES.getlist("files"):
                # print(f"test ---> {uploaded_file}")
                ImgProducts.objects.create(image=uploaded_file, product=new_product)
            
        else:
            print(form.errors)

    return HttpResponseRedirect(reverse("adminapp:products"))

@user_passes_test(lambda u: u.is_superuser)
def admin_product_remove(request, pk):
    Products.objects.get(id=pk).delete()
    return HttpResponseRedirect(reverse("adminapp:products"))

@user_passes_test(lambda u: u.is_superuser)
def admin_product_update(request, pk):
    product = Products.objects.get(id=pk)
    files = ImgProducts.objects.filter(product=pk)
    data = {
        "name": product.name,
        "ingredients": product.ingredients,
        "description": product.description,
        "category": (product.category.id, product.category.name),

        "article_four_hundred": product.article_four_hundred,
        "price_four_hundred": product.price_four_hundred,

        "article_six_hundred": product.article_six_hundred,
        "price_six_hundred": product.price_six_hundred,

        "article_eight_hundred": product.article_eight_hundred,
        "price_eight_hundred": product.price_eight_hundred,

        "article_one_thousand": product.article_one_thousand,
        "price_one_thousand": product.price_one_thousand,

        "article_two_thousand": product.article_two_thousand,
        "price_two_thousand": product.price_two_thousand
    }
    if request.method == "POST":
        
        form = CreateProductForm(request.POST, request.FILES)
        if form.is_valid():
            
            data = form.data
            product.name = data["name"]
            product.ingredients = data["ingredients"]
            product.description = data["description"]
            product.category = ProductCategories.objects.get(id=data["category"])

            product.article_four_hundred = data["article_four_hundred"]
            product.price_four_hundred = data["price_four_hundred"]

            product.article_six_hundred = data["article_six_hundred"]
            product.price_six_hundred = data["price_six_hundred"]

            product.article_eight_hundred = data["article_eight_hundred"]
            product.price_eight_hundred = data["price_eight_hundred"]

            product.article_one_thousand = data["article_one_thousand"]
            product.price_one_thousand = data["price_one_thousand"]

            product.article_two_thousand = data["article_two_thousand"]
            product.price_two_thousand = data["price_two_thousand"]
            product.save()

            for uploaded_file in request.FILES.getlist("files"):
                ImgProducts.objects.create(image=uploaded_file, product=product)
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
    ImgProducts.objects.get(id=pk).delete()
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
    Reviews.objects.get(id=pk).delete()
    return HttpResponseRedirect(reverse("adminapp:reviews"))