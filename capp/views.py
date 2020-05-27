from django.shortcuts import render
from .form import CSSForm
from django.shortcuts import redirect

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
    if request.method == 'POST': 
        form = CSSForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:         
        form = CSSForm()
    return render(request, 'review.html',{'form': form} )