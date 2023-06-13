from django.urls import path, include
from . import views


from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name="home"),
    path('promo', views.promo, name="promo"),
    path('cat1', views.category_1, name="category_1"),
    path('cat2', views.category_2, name="category_2"),
    path('cat3', views.category_3, name="category_3")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)