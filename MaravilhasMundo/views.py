from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "MaravilhasMundo/index.html")
def index2(request):
    return render(request, "MaravilhasMundo/sobre.html")

