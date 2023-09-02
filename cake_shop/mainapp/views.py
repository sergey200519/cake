from django.shortcuts import render

from mainapp.models import ProductCategories, Products, ImgProducts

from django.views.generic import DetailView


# Create your views here.
def index(request):
    context = {
        "title": "Главная",
        "product_categories": ProductCategories.objects.all(),
        "products": Products.objects.all(),
        "img_products": ImgProducts.objects.all()
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


