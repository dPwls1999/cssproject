from django.shortcuts import render, get_object_or_404
from .form import CSSForm
from django.shortcuts import redirect
from .models import CSS
# Create your views here.
def home(request):
    cafes = CSS.objects.all()
    return render(request, 'home.html', {'cafes':cafes})

def detail(request,css_id):
    css = get_object_or_404(CSS, pk = css_id)
    return render(request, 'detail.html', {'css':css})

def mainpage(request):
    return render(request, 'mainpage.html')

def edit(request):
    return render(request, 'edit.html')

def review(request):
    if request.method == 'POST': 
        form = CSSForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:         
        form = CSSForm()
    return render(request, 'review.html',{'form': form} )