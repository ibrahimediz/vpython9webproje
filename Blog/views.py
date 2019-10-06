from django.shortcuts import render,get_object_or_404
from .models import GonderiModel

def Listele(request):
    Gonderi = GonderiModel.objects.all()
    return render(request,'Blog/GListele.html',{"Gonderiler":Gonderi})


def gDetay(request,pk):
    gonderi = get_object_or_404(GonderiModel,pk=pk)
    return render(request,'Blog/gDetay.html',{"gonderi":gonderi})