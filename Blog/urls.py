from django.urls import path,include
from . import views

urlpatterns = [

    path('',views.Listele,name="gListele"),
    path('detay/<int:pk>/',views.gDetay,name="gDetay"),
    path('yeniGonderi/',views.yGonderi,name="yGonderi"),
    path('dGonderi/<int:pk>/duzenle/',views.gDuzenle,name="gDuzenle")

]