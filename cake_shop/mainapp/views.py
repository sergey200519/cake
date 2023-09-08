from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from mainapp.models import ProductCategories, Products, ImgProducts
from basketapp.models import Basket
from adminapp.models import Applications
from adminapp.forms import ApplicationsForm

from django.views.generic import DetailView



# Create your views here.
def index(request):

    if request.method == "POST":
        report_form = ApplicationsForm(request.POST)
        if report_form.is_valid():
            report_form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



    report_form = ApplicationsForm()
    context = {
        "title": "Главная",
        "product_categories": ProductCategories.objects.all(),
        "products": Products.objects.all(),
        "img_products": ImgProducts.objects.all(),
        "basket": Basket.objects.all(),
        "report_form": report_form
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


