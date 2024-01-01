from django.urls import path
from adminapp.views import IndexTemplateView, \
    ProductsListView, admin_product_create, admin_product_remove, admin_product_update, admin_product_img_remove, \
    CategoriesListView, creaate_categories, CategoryUpdateView, admin_category_remove, \
    UsersListView, admin_user_active, admin_user_notactive, \
    ReviewsListView, admin_review_approve, admin_review_cancel, admin_review_remove, \
    SlidesListView, SlideUpdateView, admin_slide_remove, \
    ApplicationsListView, admin_application_remove
    



app_name = "adminapp"
urlpatterns = [
    path("", IndexTemplateView.as_view(), name="index"),
    path("products/", ProductsListView.as_view(), name="products"),
    path("product_create/", admin_product_create, name="product_create"),
    path("product_remove/<int:pk>/", admin_product_remove, name="product_remove"),
    path("product_update/<int:pk>/", admin_product_update, name="product_update"),
    path("product_img_remove/<int:pk>/<int:id>/", admin_product_img_remove, name="product_img_remove"),

    path("categories/", CategoriesListView.as_view(), name="categories"),
    path("category_create/", creaate_categories, name="category_create"),
    path("category_update/<int:pk>/", CategoryUpdateView.as_view(), name="category_update"),
    path("category_remove/<int:pk>/", admin_category_remove, name="category_remove"),

    path("users/", UsersListView.as_view(), name="users"),
    path("user_notactive/<int:pk>/", admin_user_notactive, name="user_notactive"),
    path("user_active/<int:pk>/", admin_user_active, name="user_active"),

    path("reviews/", ReviewsListView.as_view(), name="reviews"),
    path("review_approve/<int:pk>/", admin_review_approve, name="review_approve"),
    path("review_cancel/<int:pk>/", admin_review_cancel, name="review_cancel"),
    path("review_remove/<int:pk>/", admin_review_remove, name="review_remove"),

    path("slides/", SlidesListView.as_view(), name="slides"),
    path("slides_update/<int:pk>/", SlideUpdateView.as_view(), name="slides_update"),
    path("slides_remove/<int:pk>/", admin_slide_remove, name="slide_remove"),

    path("applications/", ApplicationsListView.as_view(), name="applications"),
    path("applications_remove/<int:pk>/", admin_application_remove, name="application_remove")
]