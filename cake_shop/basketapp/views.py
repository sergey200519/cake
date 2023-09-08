from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from basketapp.models import Basket
from mainapp.models import Products

# Create your views here.

@login_required(login_url="/user/login/")
def basket(request):
    context = {
        "title": "корзина",
        "baskets": Basket.objects.all()
    }
    return  render(request,'basketapp/basket.html', context=context)


@login_required
def basket_add(request,id):
    user_select = request.user
    product = Products .objects.get(id=id)
    baskets = Basket.objects.filter(user=user_select,product=product)

    if baskets:
        basket = baskets.first()
        basket.quantity +=1
        basket.save()
    else:
        Basket.objects.create(user=user_select,product=product,quantity=1)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def basket_remove(request,basket_id):
    Basket.objects.get(id=basket_id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))