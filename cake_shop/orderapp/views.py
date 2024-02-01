from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import user_passes_test


from mainapp.models import BaseProduct
from mainapp.mixin import UserDispatchMixin, CustomDispatchMixin

from orderapp.forms import CreateOrder
from orderapp.models import OrderProduct, Order

from basketapp.models import BasketProducts

# Create your views here.
def create_order(request):
    if request.method == "POST":
        form = CreateOrder(request.POST)
        if form.is_valid() and BasketProducts.get_count(request.user):
            order = form.save()
            
            status_user = "user"
            if request.user.is_superuser:
                status_user = "admin"
            
            order.user = request.user
            order.status_completed = "notcompleted"
            order.status_owner = status_user
            order.save()
            

            for item in BasketProducts.objects.filter(user=request.user):
                base_product = BaseProduct.objects.get(article=item.article)
                OrderProduct.objects.create(
                    product=base_product,
                    image=item.image,
                    name=item.name,
                    summ=item.summ,
                    count=item.count,
                    weight_gram=item.weight_gram,
                    order=order
                )
                item.delete()
            order.calculate_summ()
        else:
            print(form.errors)
    
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

class OrdersListView(ListView, UserDispatchMixin):
    model = BaseProduct
    template_name = "orderapp/orders.html"
    context_object_name = "orders"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["object"] = reversed(Order.objects.filter(user=self.request.user))
        context["title"] = "Мои заказы"
        context["orders"] = Order.objects.filter(user=self.request.user).order_by("-id")#.reverse()
        print(context["orders"])
        return context

class OrderDetail(DetailView):
    model = Order
    template_name = "orderapp/detail.html"
    context_object_name = "order"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["order"] = Order.objects.get(id=self.kwargs["pk"])
        context["products"] = OrderProduct.objects.filter(order=context["order"])
        context["title"] = f"Заказ {context['order'].id}"

        return context
    
    def get(self, *args, **kwargs):
        order = Order.objects.get(id=self.kwargs["pk"])
        if (not self.request.user.is_superuser and order.user != self.request.user) and\
            (not self.request.user.is_superuser and order.status_owner != "admin"):
        #   pass
        # if not self.request.user.is_superuser and (order.user != self.request.user or order.status_owner != "admin"):
        #     pass
        # if (order.user != self.request.user and order.user == self.request.user.is_superuser) and order.status_owner != "admin":
            return HttpResponseRedirect(reverse("mainapp:index"))
        return super(OrderDetail, self).get(*args, **kwargs)
    

class OrderUpdateView(UpdateView, CustomDispatchMixin):
    model = Order
    # fields = ["status_delivery", ""]
    form_class = CreateOrder
    template_name = "orderapp/order_update.html"
    success_url = reverse_lazy("adminapp:orders")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = {
            "user_fullname": context["object"].user_fullname,
            "phone": context["object"].phone,
            "email": context["object"].email,
            "status_delivery": context["object"].status_delivery,
            "promo_code": context["object"].promo_code,
            "index": context["object"].index,
            "region": context["object"].region,
            "city": context["object"].city,
            "street": context["object"].street,
            "num_house": context["object"].num_house,
            "num_flat": context["object"].num_flat,
            "num_building": context["object"].num_building
        }
        context["title"] = "Админка | Заказа"
        context["order"] = Order.objects.get(id=self.kwargs["pk"])
        context["products"] = OrderProduct.objects.filter(order=context["order"])
        context["order_form"] = CreateOrder(data)
        return context

@user_passes_test(lambda u: u.is_superuser)
def complete_order(request, pk):
    order = Order.objects.get(id=pk)
    order.status_completed = "completed"
    order.save()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

@user_passes_test(lambda u: u.is_superuser)
def cancel_order(request, pk):
    order = Order.objects.get(id=pk)
    order.status_completed = "cancelled"
    order.save()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    
@user_passes_test(lambda u: u.is_superuser)
def order_remove(request, pk):
    Order.objects.get(id=pk).delete()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

@user_passes_test(lambda u: u.is_authenticated)
def repeat_order(request, pk):
    order = Order.objects.get(id=pk)
    new_order = Order.objects.create(
        status_completed="notcompleted",
        status_delivery=order.status_delivery,
        status_owner=order.status_owner,
        discount=order.discount,
        summ=order.summ,
        total_summ=order.total_summ,
        promo_code=order.promo_code,
        user_fullname=order.user_fullname,
        phone=order.phone,
        email=order.email,
        index=order.index,
        region=order.region,
        city=order.city,
        street=order.street,
        num_house=order.num_house,
        num_flat=order.num_flat,
        num_building=order.num_building,
        user=order.user
    )

    for item in OrderProduct.objects.filter(order=order):
        OrderProduct.objects.create(
            product=item.product,
            image=item.image,
            name=item.name,
            summ=item.summ,
            count=item.count,
            weight_gram=item.weight_gram,
            order=new_order
        )
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


@user_passes_test(lambda u: u.is_authenticated)
def fix_order(request, pk):
     if request.user.is_superuser:
         return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
     order = Order.objects.get(id=pk)
     order.user = request.user
     order.status_owner = "user"
     order.save()
     return HttpResponseRedirect(reverse("orderapp:orders"))