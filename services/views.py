from django.shortcuts import render

# Create your views here.
def courses(request):
    context={"course":"active"}
    return render(request,'services/courses.html',context)