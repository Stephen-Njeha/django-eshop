from django.shortcuts import render, get_object_or_404

from .models import Category, Product

from cart.forms import CartAddProductForm

def index(request, Category_slug=None):
  category = None
  categories = Category.objects.all()
  products = Product.objects.filter(available=True)
  if Category_slug:
    category = get_object_or_404(Category, slug=Category_slug)
    products = Product.objects.filter(category=category)

  context = {
    'category':category,
    'categories':categories,
    'products':products,
  }
  return render(request, 'eshop/index.html',context)

def productPage(request, Category_slug=None):
  category = None
  categories = Category.objects.all()
  products = Product.objects.filter(available=True)
  if Category_slug:
    category = get_object_or_404(Category, slug=Category_slug)
    products = Product.objects.filter(category=category)

  context = {
    'category':category,
    'categories':categories,
    'products':products,
  }
  return render(request, 'eshop/product.html',context)

def product_detail(request,id,slug,inventory_id):
  product = get_object_or_404(Product, id=id, slug=slug, inventory_id=inventory_id, available=True)
  cart_product_form = CartAddProductForm()
  context = {
    'product': product,
    'cart_product_form': cart_product_form
  }
  return render(request, 'eshop/product-detail.html',context)

def aboutDetail(request):
  return render(request, 'eshop/about.html')

def contactDetail(request):
  return render(request, 'eshop/contact.html')

def faqsDetail(request):
  return render(request, 'eshop/faqs.html')