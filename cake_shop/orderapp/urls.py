from django.urls import path
from orderapp.views import create_order, OrdersListView, OrderDetail, OrderUpdateView, order_remove, \
    complete_order, cancel_order, repeat_order, fix_order
    



app_name = "orderapp"
urlpatterns = [
    # path("", IndexTemplateView.as_view(), name="index"),
    path("create_order/", create_order, name="create_order"),
    path("orders/", OrdersListView.as_view(), name="orders"),
    path("detail/<int:pk>/", OrderDetail.as_view(), name="detail"),
    path("update/<int:pk>/", OrderUpdateView.as_view(), name="update"),
    path("remove/<int:pk>/", order_remove, name="remove"),
    path("complete_order/<int:pk>/", complete_order, name="complete_order"),
    path("cancel_order/<int:pk>/", cancel_order, name="cancel_order"),
    path("repeat_order/<int:pk>/", repeat_order, name="repeat_order"),
    path("fix_order/<int:pk>/", fix_order, name="fix_order")
]