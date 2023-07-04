from ckeditor_uploader.forms import SearchForm
from django.contrib.auth import logout, authenticate, login
from django.core.checks import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from unicodedata import category

import product
from home.models import Setting
from product.models import Product, Category, Images


# Create your views here.


def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Product.objects.all()[:4]
    category = Category.objects.all()
    dayproducts = Product.objects.all()[:4]
    lastproducts = Product.objects.all().order_by('-id')[:4]
    randomproducts = Product.objects.all().order_by('?')[:4]

    context = {'setting': setting,
               'category': category,
               'page': 'home',
               'sliderdata': sliderdata,
               'dayproducts': dayproducts,
               'lastproducts': lastproducts,
               'randomproducts': randomproducts
               }
    return render(request, 'index.html', context)


def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting,
               'category': category,
               'page': 'home',
               }
    return render(request, 'hakkimizda.html', context)


def referanslar(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting,
               'category': category,
               'page': 'home',
               }
    return render(request, 'referanslarimiz.html', context)


def iletisim(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting,
               'category': category,
               'page': 'home'
               }
    return render(request, 'iletisim.html', context)


def category_products(request, id, slug):

    category = Category.objects.all()
    products = Product.objects.filter(category_id=id)
    context = {'products': products,
               'category': category,
               'slug': slug
               }
    return render(request, 'products.html', context)


def product_search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            category = Category.objects.all()
            q = form.cleaned_data['q']
            products = Product.objects.filter(title__icontains=q)
            context = {'products': products,
                       'category': category,
                       }
            return render(request, 'product_search.html', context)
            return HttpResponseRedirect('/')


def product_detail(request,id,slug):
    category = Category.objects.all()
    product = Product.objects.get(pk=id)
    images = Images.objects.filter(product_id=id)
    context = {'product': product,
               'category': category,
               'images': images,
               }

    return render(request, 'product_detail.html',context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
def login_view(request):
    if request.method == 'POST':

     username = request.POST['username']
     password = request.POST['password']
     user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)

    else:
        messages.error(request, "Login hatası!")
        return HttpResponseRedirect('/login')
    category = Category.objects.all()
    context = {'category': category,
               }
    return render(request, 'login.html', context)







