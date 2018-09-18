from django.conf.urls import url

from django.urls import path

from . import views

app_name = 'eshop'

urlpatterns = [
  path('home/', views.index, name='home'),
  path('help/', views.faqsDetail, name='help'),
  path('about/', views.aboutDetail, name='about_detail'),
  path('contact/', views.contactDetail, name='contact_detail'),
  path('product/', views.productPage,name="product"),
  url(r'^(?P<category_slug>[-\w]+)/$', views.productPage, name='product-by-category'),
  url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/(?P<inventory_id>[-\w]+)$',views.product_detail,name='product-detail'),
]