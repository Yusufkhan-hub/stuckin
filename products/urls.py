from django.urls import path
from . import views
from .views import product,collection#,collection,get_collection
# app_name='products'


urlpatterns = [
    # path('collections/<slug:slug>/',collection.as_view(),name="collection"),
    # path('get_collections/<slug:slug>/',get_collection.as_view(),name="getcollection"),
    # path('product/<slug:slug>/',product.as_view(),name="product"),
    path('collection',views.collection,name="collection"),
    path('product/<str:shoe_id>/',views.product,name="product"),
]
