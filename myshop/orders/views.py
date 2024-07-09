from cart.cart import Cart
from django.shortcuts import redirect, render

from .forms import OrderCreateForm
from .models import OrderItem
from .tasks import order_created


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()

            # Create and Save Order Items
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )

            # clear the cart
            cart.clear()

            # launch asynchronous task to message broker
            # You call the delay() method of the task to execute it asynchronously. The task will be added to the message queue and executed by the Celery worker as soon as possible.
            order_created.delay(order.id)

            # return render(request, 'orders/order/created.html', {'order': order})

            # set the order in session
            request.session['order_id'] = order.id

            return redirect('payment.process')
    else:
        form = OrderCreateForm()
    return render(
        request,
        'orders/order/create.html',
        {'cart': cart, 'form': form}
    )
