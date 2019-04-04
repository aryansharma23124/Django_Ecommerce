from django.conf.urls import url, include
from django.urls import path
from .views import all_products,compare,buy,add_cart,view_cart,pay

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^compare/(?P<name>.+?)/$', compare, name='compare'),
    url(r'^buy/(?P<id>.+?)/$',buy, name='buy'),
    url(r'^add_cart/(?P<id>.+?)/$', add_cart, name='add_cart'),
    url(r'^cart/view_cart/$', view_cart, name='cart_view'),
    url(r'^pay/(?P<id>.+?)/$',pay, name='pay'),
    # url(r'^delete/(?P<id>\d+)/$', delete, name="delete"),
    ]