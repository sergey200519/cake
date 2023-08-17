from django.shortcuts import render

from mainapp.models import ProductCategories, Products, ImgProducts

# Create your views here.
def index(request):
    context = {
        'title': "Главная",
        "product_categories": ProductCategories.objects.all(),
        "products": Products.objects.all(),
        "img_products": ImgProducts.objects.all()
    }
    return  render(request,'mainapp/index.html', context=context) 