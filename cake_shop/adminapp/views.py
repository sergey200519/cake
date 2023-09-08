from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView, CreateView, DeleteView, UpdateView, DetailView

from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from django.forms import modelformset_factory, formset_factory, inlineformset_factory

from mainapp.models import Products, ProductCategories, ImgProducts

from adminapp.forms import CreateProductForm, ImageForm, BaseArticleFormSet, UploadFileForm

from adminapp.models import Applications

from django.contrib.auth.decorators import user_passes_test

from mainapp.mixin import CustomDispatchMixin

import ast



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
        context["title"] = "Админка | Товары"
        return context
    

@user_passes_test(lambda u: u.is_superuser)
def admin_product_create(request):
    if request.method == "POST":
        form = CreateProductForm(request.POST, request.FILES)
        formset = UploadFileForm(request.POST, request.FILES)
        
        print(form.data)
        if form.is_valid():
            data = form.data
            name = data["name"]
            ingredients = data["ingredients"]
            quantity = data["quantity"]
            price = data["price"]
            description = data["description"]
            category = ProductCategories.objects.get(id=data["category"])
            new_product = Products.objects.create(name=name, ingredients=ingredients, quantity=quantity, price=price, description=description, category=category)

            for uploaded_file in request.FILES.getlist("files"):
                # print(f"test ---> {uploaded_file}")
                ImgProducts.objects.create(image=uploaded_file, product=new_product)
            return HttpResponseRedirect(reverse("adminapp:products"))
        else:
            print(form.errors)
    else:
        form = CreateProductForm()
        formset = UploadFileForm()
    form = CreateProductForm(request.POST, request.FILES)
    formset = UploadFileForm(request.POST, request.FILES)


    context = {
        "title": "Админка | Регистрация",
        "form": CreateProductForm(),
        # "formset": ImageFormSet
        "formset": formset
    }

    return render(request,"adminapp/product_create.html",context)


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
        "quantity": product.quantity,
        "price": product.price,
        "description": product.description,
        "category": (product.category.id, product.category.name)
    }
    print(data)
    if request.method == "POST":
        
        form = CreateProductForm(request.POST, request.FILES)
        if form.is_valid():
            
            data = form.data
            product.name = data["name"]
            product.ingredients = data["ingredients"]
            product.quantity = data["quantity"]
            product.price = data["price"]
            product.description = data["description"]
            product.category = ProductCategories.objects.get(id=data["category"])
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
        return context
    


class CategoryCreateView(CreateView, CustomDispatchMixin):
    model = ProductCategories
    fields = ["name"]
    template_name = "adminapp/category_create.html"
    success_url = reverse_lazy("adminapp:categories")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Админка | создание категории"
        return context
    


class CategoryUpdateView(UpdateView, CustomDispatchMixin):
    model = ProductCategories
    fields = ["name"]
    template_name = "adminapp/category_update.html"
    success_url = reverse_lazy("adminapp:categories")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Админка | изменение категории"
        return context


# class CategoryDeleteView(DeleteView):
#     model = ProductCategories
#     template_name = "adminapp/category_update.html"
#     success_url = reverse_lazy("adminapp:categories")

@user_passes_test(lambda u: u.is_superuser)
def admin_category_remove(request, pk):
    ProductCategories.objects.get(id=pk).delete()
    return HttpResponseRedirect(reverse("adminapp:categories"))


class ApplicationsListView(ListView, CustomDispatchMixin):
    model = Applications
    template_name = "adminapp/reports_admin.html"
    title =  "Админка | Заявки"

    


class ApplicationsDeleteView(DeleteView, CustomDispatchMixin):
    model = Applications
    template_name = "adminapp/report_detail.html"
    success_url = reverse_lazy("adminapp:reports")

@user_passes_test(lambda u: u.is_superuser)
def admin_applications_remove(request, pk):
    Applications.objects.get(id=pk).delete()
    return HttpResponseRedirect(reverse("adminapp:reports"))