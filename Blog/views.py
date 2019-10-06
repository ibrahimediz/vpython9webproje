from django.shortcuts import render
from .models import GonderiModel

def Listele(request):
    Gonderi = GonderiModel.objects.all()
    return render(request,'Blog/GListele.html',{"Gonderiler":Gonderi})