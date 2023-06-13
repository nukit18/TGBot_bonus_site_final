from django.shortcuts import render
from .models import Goods, CategoryGoods, Promotions


def index(request):
    goods_list = Goods.objects.order_by('-id')
    categories_names = CategoryGoods.objects.all()
    list_pages = ["category_1", "category_2", "category_3"]
    list_selections = ["font-weight: bold;", "", "", ""]
    return render(request, 'goods_list/index.html',
                  {
                      'title': "Список товаров - главная",
                      'goods_list': goods_list,
                      'categories_names': categories_names,
                      'list_pages': list_pages,
                      'list_selections': list_selections
                  })


def category_1(request):
    goods_list = Goods.objects.filter(category="category_1").order_by('-id')
    categories_names = CategoryGoods.objects.all()
    list_pages = ["category_1", "category_2", "category_3"]
    list_selections = ["", "font-weight: bold;", "", ""]
    return render(request, 'goods_list/index.html',
                  {
                      'title': "Список товаров - главная",
                      'goods_list': goods_list,
                      'categories_names': categories_names,
                      'list_pages': list_pages,
                      'list_selections': list_selections
                  })


def category_2(request):
    goods_list = Goods.objects.filter(category="category_2").order_by('-id')
    categories_names = CategoryGoods.objects.all()
    list_pages = ["category_1", "category_2", "category_3"]
    list_selections = ["", "", "font-weight: bold;", ""]
    return render(request, 'goods_list/index.html',
                  {
                      'title': "Список товаров - главная",
                      'goods_list': goods_list,
                      'categories_names': categories_names,
                      'list_pages': list_pages,
                      'list_selections': list_selections
                  })


def category_3(request):
    goods_list = Goods.objects.filter(category="category_3").order_by('-id')
    categories_names = CategoryGoods.objects.all()
    list_pages = ["category_1", "category_2", "category_3"]
    list_selections = ["", "", "", "font-weight: bold;"]
    return render(request, 'goods_list/index.html',
                  {
                      'title': "Список товаров - главная",
                      'goods_list': goods_list,
                      'categories_names': categories_names,
                      'list_pages': list_pages,
                      'list_selections': list_selections
                  })


def promo(request):
    promo_list = Promotions.objects.order_by('-id')
    return render(request, 'goods_list/promo.html',
                  {
                      'title': "Список акций",
                      'promo_list': promo_list,
                  })