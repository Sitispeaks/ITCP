from django.shortcuts import render
from .models import alumni_info

# Create your views here.

def alumni(request):
    alums=alumni_info.objects.all()
    context={"alumni":"active","alumnis":alums}
    return render(request,'edu/alumnis.html',context)

