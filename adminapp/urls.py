from django.urls import path
# from django.urls import re_path
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
# urlpatterns = [
#     re_path(r"^users/new/$", adminapp.user_new, name="user_new"),
#     re_path(r"^users/read/$", adminapp.UsersListView.as_view(), name="users"),
#     re_path(r"^users/update/(?P<pk>\d+)/$", adminapp.user_update, name="user_update"),
#     re_path(r"^users/deactive/(?P<pk>\d+)/$", adminapp.user_deactive, name="user_deactive"),
#     re_path(r"^users/delete/(?P<pk>\d+)/$", adminapp.user_delete, name="user_delete"),
#     re_path(
#         r"^categories/new/$",
#         adminapp.AdminProductCategoryCreateView.as_view(),
#         name="category_new",
#     ),
#     re_path(r"^categories/read/$", adminapp.categories, name="categories"),
#     re_path(
#         r"^categories/update/(?P<pk>\d+)/$",
#         adminapp.AdminProductCategoryUpdateView.as_view(),
#         name="category_update",
#     ),
#     re_path(
#         r"^categories/delete/(?P<pk>\d+)/$",
#         adminapp.AdminProductCategoryDeleteView.as_view(),
#         name="category_delete",
#     ),
#     re_path(r"^goods/new/(?P<pk>\d+)/$", adminapp.good_new, name="good_new"),
#     re_path(r"^goods/read/category/(?P<pk>\d+)/$", adminapp.goods, name="goods"),
#     re_path(
#         r"^goods/read/(?P<pk>\d+)/$",
#         adminapp.AdminProductDetailView.as_view(),
#         name="good_read",
#     ),
#     re_path(r"^goods/update/(?P<pk>\d+)/$", adminapp.good_update, name="good_update"),
#     re_path(r"^goods/delete/(?P<pk>\d+)/$", adminapp.good_delete, name="good_delete"),
# ]
