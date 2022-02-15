from django.shortcuts import render

from django.shortcuts import get_object_or_404, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.db import transaction

from django.forms import inlineformset_factory

from django.views.generic import ListView, DeleteView, UpdateView, CreateView
from django.views.generic.detail import DetailView

from cartapp.models import CartItem
from ordersapp.models import Order, OrderItem
from ordersapp.forms import OrderItemForm


def slug(request):
    page_title = 'Заказы'
    print(f'type={type(request.user)} request.user={request.user}')
    context = {
        'page_title': page_title,
        'message': 'контроллер без аргументов',
        }
    return render(request, 'ordersapp/temp.html', context=context)


def slug1(request, pk):
    page_title = 'Заказы'
    print(f'type={type(request.user)} request.user={request.user}')
    context = {
        'page_title': page_title,
        'message': 'контроллер с 1 аргументом',
        }
    return render(request, 'ordersapp/temp.html', context=context)


class OrderList(ListView):
    Model = Order

    def get_queryset(self):
        return self.Model.objects.filter(user=self.request.user)  # помним, что Model=Order


# class OrderCreate(CreateView):
#     Model = Order
#     fields = []
#     success_url = reverse_lazy('order:order_list')
#     cart_items = CartItem.get_items(self.request.user)
#     if len(cart_items):
#         OrderFormSet = inlineformset_factory(Order,
#                                              OrderItem,
#                                              form=OrderItemForm,
#                                              extra=len(cart_items))
#         formset = OrderFormSet()
#         for num, form in enumerate(formset.forms):
#             form.initial['product'] = cart_items[num].product
#             form.initial['quantity'] = cart_items[num].qtty
#         cart_items.delete()
#     else:
#         formset = OrderFormSet()

