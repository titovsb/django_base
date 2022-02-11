from django.urls import path
import adminapp.views as adminapp

app_name = "adminapp"

urlpatterns = [
    path("users/new/", adminapp.user_new, name="user_new"),
    path("users/read/", adminapp.UsersListView.as_view(), name="users"),
    path("users/update/<int:pk>/", adminapp.user_update, name="user_update"),
    path("users/deactive/<int:pk>/", adminapp.user_deactive, name="user_deactive"),
    path("users/delete/<int:pk>/", adminapp.user_delete, name="user_delete"),
    path(
        "categories/new/",
        adminapp.AdminProductCategoryCreateView.as_view(),
        name="category_new",
    ),
    path("categories/read/", adminapp.categories, name="categories"),
    path(
        "categories/update/<int:pk>/",
        adminapp.AdminProductCategoryUpdateView.as_view(),
        name="category_update",
    ),
    path(
        "categories/delete/<int:pk>/",
        adminapp.AdminProductCategoryDeleteView.as_view(),
        name="category_delete",
    ),
    path("goods/new/<int:pk>/", adminapp.good_new, name="good_new"),
    path("goods/read/category/<int:pk>/", adminapp.goods, name="goods"),
    path(
        "goods/read/<int:pk>/",
        adminapp.AdminProductDetailView.as_view(),
        name="good_read",
    ),
    path("goods/update/<int:pk>/", adminapp.good_update, name="good_update"),
    path("goods/delete/<int:pk>/", adminapp.good_delete, name="good_delete"),
]
