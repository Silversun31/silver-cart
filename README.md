# silver-cart

## Para que funcione:
### Añadir a settings context_processor el siguiente elemento:  
    'cart.context_processor.cart_total_amount'  
### Añadir en las variables de settings:  
    CART_SESSION_ID = 'cart'  
### Cambiar en las views por su propio modelo producto el import  
    from store.models import Product  
### En su producto son obligatorios los campos:  
    name = models.CharField(max_length=255)  
    image = models.ImageField(upload_to=’products/’)  
    price = models.FloatField()  
### El carrito pone a disposicion las siguientes urls:  
    urlpatterns = [  
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),  
    path('cart/item_clear/<int:id>/', views.item_clear, name='cart_item_clear'),  
    path('cart/item_increment/<int:id>/', views.item_increment, name='cart_item_increment'),  
    path('cart/item_decrement/<int:id>/', views.item_decrement, name='cart_item_decrement'),  
    path('cart/cart_clear/', views.cart_clear, name='cart_cart_clear'),  
    path('cart/cart-detail/', views.cart_detail, name='cart_cart_detail'),  
    ]  
  
## Esto es una modificacion del carrito disponible en https://pypi.org/project/django-shopping-cart/#description con proyecto en git https://github.com/MahmudulHassan5809/django-shopping-cart
