from django.shortcuts import render,get_object_or_404,redirect
from .models import IletisimModel
from .forms import IletisimForm
from django.utils import timezone

def Liste(request):
    Ileti = IletisimModel.objects.all()
    return render(request,'Iletisim/IletiListele.html',{"Iletilerimiz":Ileti})


def IletiDetay(request,pk):
    Ileti = get_object_or_404(IletisimModel,pk=pk)
    return render(request,'Iletisim/IletiDetay.html',{"ileti":Ileti})

def yeniIleti(request):
    if request.method == "POST":
        form = IletisimForm(request.POST, request.FILES)
        if form.is_valid():
            ileti = form.save(commit=False)
            ileti.save()
            return redirect('IletiDetay',pk=ileti.pk)
    else:
        form = IletisimForm()
    return render(request,'Iletisim/yIleti.html',{"form":form})
