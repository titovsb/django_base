from django.shortcuts import render

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import HttpResponseRedirect, get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from authapp.models import DebiUserProfile, DebiUser
from mainapp.models import Product, ProductCategory

from adminapp.forms import AdminDebiUserEditForm, AdminDebiUserProfileEditForm, AdminProductEditForm, AdminProductCategoryEditForm
from authapp.forms import DebiUserCreationForm


# Create your views here.


class UsersListView(ListView):
    model = DebiUser
    template_name = "adminapp/users.html"

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


@user_passes_test(lambda u: u.is_superuser)
def user_deactive(request, pk):
    # page_title = 'удаление пользователя'
    user = get_object_or_404(DebiUser, pk=pk)
    user.is_active = not user.is_active
    user.save()
    return HttpResponseRedirect(reverse("console:users"))
    #
    # user = get_object_or_404(DebiUser, pk=pk)
    #
    # if request.method == 'POST':
    #     user.is_active = False
    #     user.save()
    #     return HttpResponseRedirect(reverse('console:users'))
    #
    # context = {
    #     'page_title': page_title,
    #     'user_to_delete': user,
    #     }
    #
    # return render(request, 'adminapp/user_delete.html', context=context)


@user_passes_test(lambda u: u.is_superuser)
def user_delete(request, pk):
    page_title = "удаление пользователя навсегда"

    user = get_object_or_404(DebiUser, pk=pk)

    if request.method == "POST":
        user.delete()
        return HttpResponseRedirect(reverse("console:users"))

    context = {
        "page_title": page_title,
        "user_to_delete": user,
    }

    return render(request, "adminapp/user_delete.html", context=context)


@user_passes_test(lambda u: u.is_superuser)
def user_update(request, pk):
    page_title = "редактирование пользователя"
    message = ""
    edit_user = get_object_or_404(DebiUser, pk=pk)
    # print(f'edit_user={edit_user}, edit_user.pk={edit_user.pk}')
    if request.method == "POST":
        user_form = AdminDebiUserEditForm(request.POST, instance=edit_user)
        profile_form = AdminDebiUserProfileEditForm(
            request.POST, request.FILES, instance=edit_user.profile
        )
        print(f"edit_user.profile={edit_user.profile}")
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect(reverse("console:users"))
        message = "проверьте правильность заполнения полей формы"
    else:
        user_form = AdminDebiUserEditForm(instance=edit_user)
        profile_form = AdminDebiUserProfileEditForm(instance=edit_user.profile)
    context = {
        "page_title": page_title,
        "user_form": user_form,
        "profile_form": profile_form,
        "message": message,
    }
    return render(request, "adminapp/user_update.html", context=context)


@user_passes_test(lambda u: u.is_superuser)
def user_new(request):
    page_title = "создать нового пользователя"
    if request.method == "POST":
        form = DebiUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(f"user={user} user.pk={user.pk}")
            user.is_active = True
            user.save()
            return HttpResponseRedirect(reverse("console:users"))
    else:
        form = DebiUserCreationForm()
    context = {
        "page_title": page_title,
        "user_form": form,
    }
    return render(request, "adminapp/user_update.html", context=context)


@user_passes_test(lambda u: u.is_superuser)
def categories(request):
    page_title = "админка/категории"

    categories = ProductCategory.objects.all()

    context = {
        "page_title": page_title,
        "objects": categories,
    }

    return render(request, "adminapp/categories.html", context=context)


class AdminProductCategoryCreateView(CreateView):
    model = ProductCategory
    # по умолчанию имя файла должно быть 'productcategory_form.html'
    template_name = "adminapp/category_update.html"
    success_url = reverse_lazy("console:categories")
    fields = "__all__"


class AdminProductCategoryUpdateView(UpdateView):
    model = ProductCategory
    # по умолчанию имя файла должно быть 'productcategory_form.html'
    template_name = "adminapp/category_update.html"
    success_url = reverse_lazy("console:categories")
    fields = "__all__"

    def get_context_data(self, **kwargs):
        """метод передает контекст в шаблон"""
        context = super().get_context_data(**kwargs)
        context["page_title"] = "категории/редактирование"
        return context


class AdminProductCategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = "adminapp/category_delete.html"
    success_url = reverse_lazy("console:categories")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


@user_passes_test(lambda u: u.is_superuser)
def goods(request, pk):
    page_title = 'продукты категории'
    category = get_object_or_404(ProductCategory, pk=pk)
    products = Product.objects.filter(category__pk=pk).order_by('name')
    context = {
        'page_title': page_title,
        'category': category,
        'objects': products,
        }
    return render(request, 'adminapp/goods.html', context=context)

class AdminProductDetailView(DetailView):
    model = Product
    # по дефолту было б: "mainapp/product_detail.html"
    template_name = 'adminapp/good_read.html'

def good_new(request, pk):
    page_title = 'продукт создание'
    category = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        product_form = AdminProductEditForm(request.POST, requests.FILES)
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect(reverse('console:goods', args=[pk]))
    else:
        # начальное значение поля в форме задаем
        product_form = AdminProductEditForm(initial={'category': category})
    context = {
        'page_title': page_title,
        'update_form': product_form,
        'category': category,
        }
    return render(request, 'adminapp/good_update.html', context=context)

def good_update(request, pk):
    page_title = 'продукт/редактирование'
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        update_form = AdminProductEditForm(request.POST, request.FILES, instance=product)
        if update_form.is_valid():
            update_form.save()
            return HttpResponseRedirect(reverse('console:good_update', args=[product.pk]))
    else:
        update_form = AdminProductEditForm(instance=product)
    context = {
        'page_title': page_title,
        'category': product.category,
        'update_form': update_form,
        }
    return render(request, 'adminapp/good_update.html', context=context)

def good_delete(request, pk):
    page_title = 'удаление продукта'
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.is_active = False
        product.save()
        return HttpResponseRedirect(reverse('console:goods', args=[product.category.pk]))
    context = {
        'page_title': page_title,
        'product': product,
        }
    return render(request, 'adminapp/good_delete.html', context=context)
