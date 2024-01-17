from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt


from mainapp.models import Product, BaseProduct, ImgProduct, ExclusiveProducts, ImgExclusive
from basketapp.models import BasketProducts

# Create your views here.
def product_add_basket(request):
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        if request.method == "GET":
            context = {}
            if request.user.is_authenticated:
                article=request.headers.get("productArticle")
                product_id=request.headers.get("productId")
                
                product_base = BaseProduct.objects.get(article=article)
                product = Product.objects.get(id=product_id)
                
                if BasketProducts.objects.filter(article=article).exists():
                    basket_products = BasketProducts.objects.get(article=article)
                    basket_products.count += 1
                    basket_products.save()
                else:
                    if ImgProduct.objects.filter(product=product).exists():
                        img = ImgProduct.objects.filter(product=product)[0]
                        BasketProducts.objects.create(image=img.image, \
                                                    name=product.name, count=1, \
                                                    weight=product_base.weight, \
                                                    discount=0, \
                                                    price=product_base.price, \
                                                    summ=0, \
                                                    article=product_base.article, \
                                                    user=request.user)
                    else:
                        BasketProducts.objects.create(name=product.name, count=1, \
                                                    weight=product_base.weight, \
                                                    discount=0, \
                                                    price=product_base.price, \
                                                    summ=0, \
                                                    article=product_base.article, \
                                                    user=request.user)
                context["status"] = "success"
                context["basket_products"] = render_to_string("mainapp/popups/order_popup.html", {"baskets": BasketProducts.objects.filter(user=request.user)})
                context["count"] = BasketProducts.get_count(user=request.user)
            elif not request.user.is_authenticated:
                context["status"] = "userNotAuthenticated"
            else:
                context["status"] = "error"
            return JsonResponse(context)


def exclusive_add_basket(request):
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        if request.method == "GET":
            context = {}
            if request.user.is_authenticated:
                article=request.headers.get("productArticle")
                product_id=request.headers.get("productId")
                
                product_base = BaseProduct.objects.get(article=article)
                product = ExclusiveProducts.objects.get(id=product_id)
                
                if BasketProducts.objects.filter(article=article).exists():
                    basket_products = BasketProducts.objects.get(article=article)
                    basket_products.count += 1
                    basket_products.save()
                else:
                    if ImgExclusive.objects.filter(exclusive=product).exists():
                        img = ImgExclusive.objects.filter(exclusive=product)[0]
                        BasketProducts.objects.create(image=img.image, \
                                                    name=product.name, count=1, \
                                                    weight=product_base.weight, \
                                                    discount=0, \
                                                    price=product_base.price, \
                                                    summ=0, \
                                                    article=product_base.article, \
                                                    user=request.user)
                    else:
                        BasketProducts.objects.create(name=product.name, count=1, \
                                                    weight=product_base.weight, \
                                                    discount=0, \
                                                    price=product_base.price, \
                                                    summ=0, \
                                                    article=product_base.article, \
                                                    user=request.user)
                context["status"] = "success"
                context["basket_products"] = render_to_string("mainapp/popups/order_popup.html", {"baskets": BasketProducts.objects.filter(user=request.user)})
                context["count"] = BasketProducts.get_count(user=request.user)
            elif not request.user.is_authenticated:
                context["status"] = "userNotAuthenticated"
            else:
                context["status"] = "error"
            return JsonResponse(context)
        
@csrf_exempt
def delete_basket_product(request, pk):
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        if request.method == "GET":
            try:
                BasketProducts.objects.get(id=pk).delete()
                context = {
                    "basket_products": render_to_string("mainapp/popups/order_popup.html", {"baskets": BasketProducts.objects.filter(user=request.user)}),
                    "count": BasketProducts.get_count(user=request.user),
                    "status": "success"
                }
            except:
                context = {
                    "status": "error"
                }
            return JsonResponse(context)