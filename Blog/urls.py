from django.urls import path,include
from . import views

urlpatterns = [

    path('',views.Listele,name="gListele"),
    path('detay/<int:pk>/',views.gDetay,name="gDetay")

]