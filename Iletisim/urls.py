from django.urls import path
from . import views

urlpatterns = [

    path('',views.Liste,name="IletiListe"),
    path('detay/<int:pk>',views.IletiDetay,name="IletiDetay"),
    path('yeni/',views.yeniIleti,name='yeniIleti')

]