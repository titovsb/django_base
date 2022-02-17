from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CartItem
from django.urls import reverse

from mainapp.context_processors import ctx_cart

from mainapp.models import Product

from django.template.loader import render_to_string
from django.http import JsonResponse

from django.conf import settings
# from authapp.views import login


# Create your views here.

@login_required(login_url=settings.LOGIN_URL)
def cart(request):
    page_title = 'корзина покупок'
    # cart_items = CartItem.objects.filter(user=request.user).order_by('product__category')
    context = {
        'page_title': page_title,
        # 'cart_items': cart_items,
        }
    return render(request, 'cartapp/cart.html', context=context)


@login_required(login_url=settings.LOGIN_URL)
def cart_add(request, pk):
    # если залогинились то снова на страничку товара
    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('primary:index', args=[pk]))
    product = get_object_or_404(Product, pk=pk)
    cart = CartItem.objects.filter(user=request.user, product=product).first()
    if not cart:
        cart = CartItem(user=request.user, product=product)
    cart.qtty += 1
    cart.save()
    # возвращаемся на ссылку с которой пришли
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url=settings.LOGIN_URL)
def cart_remove(request, pk):
    page_title = 'удалить товар из заказа'
    item = get_object_or_404(CartItem, pk=pk)
    if request.method == 'POST':
        item.delete()
        return HttpResponseRedirect(reverse('cart:cart'))
    context = {
        'page_title': page_title,
        'item': item,
        }
    print('TEST', context)
    return render(request, 'cartapp/item_delete.html', context=context)


@login_required(login_url=settings.LOGIN_URL)
def cart_edit(request, pk, qtty):
    if request.is_ajax():
        quantity = int(qtty)
        new_cart_item = CartItem.objects.get(pk=int(pk))
        if quantity > 0:
            new_cart_item.qtty = quantity
            new_cart_item.save()
        else:
            new_cart_item.delete()
        # cart_items = ctx_cart(request)
        # total_items = cart_items.total_quantity
        # total_cost = cart_items.total_cost
        context = {
            # 'cart_items': cart_items,
            # 'total_items': total_items,
            # 'total_cost': total_cost,
            }
        result = render_to_string('cartapp/includes/cart_list.html',
                                  context=context,
                                  request=request)

        return JsonResponse({'result': result})
