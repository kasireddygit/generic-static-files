from django.shortcuts import render

# Create your views here.
def genericstatic(request):
    return render(request,'genericstatic.html')
