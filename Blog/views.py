from django.shortcuts import render,get_object_or_404,redirect
from .models import GonderiModel
from .forms import GonderiForm
from django.contrib.auth.models import User
from django.utils import timezone

def Listele(request):
    Gonderi = GonderiModel.objects.all()
    return render(request,'Blog/GListele.html',{"Gonderiler":Gonderi})


def gDetay(request,pk):
    gonderi = get_object_or_404(GonderiModel,pk=pk)
    return render(request,'Blog/gDetay.html',{"gonderi":gonderi})

def yGonderi(request):
    if request.method == "POST":
        form = GonderiForm(request.POST)
        if form.is_valid():
            gonderi = form.save(commit=False)
            ben = User.objects.get(username="admin")
            gonderi.yazar = ben
            gonderi.yayim_zaman = timezone.now()
            gonderi.save()
            return redirect('gDetay',pk=gonderi.pk)
    else:
        form = GonderiForm()
    return render(request,'Blog/yGonderi.html',{"form":form})


def gDuzenle(request,pk):
    gonderi = get_object_or_404(GonderiModel,pk=pk)
    if request.method == "POST":
        form = GonderiForm(request.POST,instance=gonderi)
        if form.is_valid():
            gonderi = form.save(commit=False)
            ben = User.objects.get(username="admin")
            gonderi.yazar = ben
            gonderi.yayim_zaman = timezone.now()
            gonderi.save()
            return redirect('gDetay',pk=gonderi.pk)
    else:
        form = GonderiForm(instance=gonderi)
    return render(request,'Blog/dGonderi.html',{"form":form})