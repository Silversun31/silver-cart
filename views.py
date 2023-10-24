# Create your views here.
from django.http import HttpResponse, JsonResponse
from store.models import Product
from django.contrib.auth.decorators import login_required
from cart import Cart


@login_required
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return HttpResponse(status=200)


@login_required
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return HttpResponse(status=200)


@login_required
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return HttpResponse(status=200)


@login_required
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return HttpResponse(status=200)


@login_required
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return HttpResponse(status=200)


@login_required
def cart_detail(request):
    return JsonResponse({'cart': Cart(request)})