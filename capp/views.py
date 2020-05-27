from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def detail(request):
    return render(request, 'detail.html')

def mainpage(request):
    return render(request, 'mainpage.html')

def edit(request):
    return render(request, 'edit.html')

def review(request):
    return render(request, 'review.html')