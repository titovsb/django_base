from cartapp.models import CartItem


def ctx_cart(request):
    '''
    Контекстный процессор для прямого доступа к корзине из шаблона
    Не забыть добавить в settings.py
    'mainapp.context_processors.cart'
    '''
    print(f'context processor "cart" works')
    cart_items = []
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user).order_by('product__category')

    return {
        'cart_items': cart_items,
        }
