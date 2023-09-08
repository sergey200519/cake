from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView, CreateView, DeleteView, UpdateView, DetailView

from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from django.forms import modelformset_factory, formset_factory, inlineformset_factory

from mainapp.models import Products, ProductCategories, ImgProducts

from adminapp.forms import CreateProductForm, ImageForm, BaseArticleFormSet, UploadFileForm

import ast



# Create your views here.
class IndexTemplateView(TemplateView):
    template_name = "adminapp/admin.html"
    title = "Главня страница aдминки"


class ProductsListView(ListView):
    model = Products
    template_name = "adminapp/products_admin.html"
    title =  "Админка | Товары"
    context_object_name = "products"


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



def admin_product_remove(request, pk):
    Products.objects.get(id=pk).delete()
    return HttpResponseRedirect(reverse("adminapp:products"))


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


def admin_product_img_remove(request, pk, id):
    ImgProducts.objects.get(id=pk).delete()
    return HttpResponseRedirect(reverse("adminapp:product_update", args=[id]))


class CategoriesListView(ListView):
    model = ProductCategories
    template_name = "adminapp/categories_admin.html"
    title =  "Админка | Категории"
    context_object_name = "product_categories"


class CategoryCreateView(CreateView):
    model = ProductCategories
    fields = ["name"]
    template_name = "adminapp/category_create.html"

    success_url = reverse_lazy("adminapp:categories")


class CategoryUpdateView(UpdateView):
    model = ProductCategories
    fields = ["name"]
    template_name = "adminapp/category_update.html"

    success_url = reverse_lazy("adminapp:categories")


# class CategoryDeleteView(DeleteView):
#     model = ProductCategories
#     template_name = "adminapp/category_update.html"
#     success_url = reverse_lazy("adminapp:categories")

def admin_category_remove(request, pk):
    ProductCategories.objects.get(id=pk).delete()
    return HttpResponseRedirect(reverse("adminapp:categories"))
