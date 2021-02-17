from django.shortcuts import render
from .models import alum

# Create your views here.

def alumni(request):
    alums=alum.objects.all()
    context={"alumni":"active","alumnis":alums}
    return render(request,'edu/alumnis.html',context)

