from django.shortcuts import render

# Create your views here.

def carta(request):
    return render(request,'core/carta.html')