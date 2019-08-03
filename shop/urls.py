from django.urls import path
from . import views
 
app_name = 'shop'
urlpatterns = [

    # path('', views.index),
    # path('<int:category_id>/', views.category, name='category'),
    path('',views.allProdCat, name="allProdCat"),
    path('<slug:c_slug>/',views.allProdCat,name='products_by_category'),
    path('product/<int:prod_id>/',views.productsInfo, name="productsInfo"),
    path('<slug:c_slug>/<slug:product_slug>/', views.ProdCatDetail, name="ProdCatDetail"),
]