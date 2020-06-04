from django.shortcuts import render, get_object_or_404
from .form import CSSForm, CommentForm
from django.shortcuts import redirect
from .models import CSS
from account.models import CustomModel
from django.utils import timezone




# Create your views here.
def home(request):
    cafes = CSS.objects.all()
    return render(request, 'home.html', {'cafes':cafes})

def detail(request,css_id):
    css = get_object_or_404(CSS, pk = css_id)
    if request.method == "POST":
        cform = CommentForm(request.POST)
        if cform.is_valid():
            comment = cform.save(commit=False)
            comment.post = css
            comment.save()
            return redirect('/detail/'+ str(css.id))
    else:
        cform = CommentForm()
    return render(request, 'detail.html', {'css':css, 'cform': cform})

def mypage(request):
    return render(request, 'mypage.html')

# def edit(request, css_id):
#     css = get_object_or_404(CSS, pk = css_id)
#     return render(request, 'edit.html', {'css':css})
def edit(request, css_id):
    css = get_object_or_404(CSS, pk = css_id)
    if request.method == 'POST': 
        form = CSSForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            css.title=form.cleaned_data['title']
            css.area= form.cleaned_data['area']
            css.time= form.cleaned_data['time']
            css.mood= form.cleaned_data['mood']
            css.floor=form.cleaned_data['floor']
            css.toilet=form.cleaned_data['toilet']
            css.smoke=form.cleaned_data['smoke']
            css.elevator=form.cleaned_data['elevator']
            css.pet= form.cleaned_data['pet']
            css.add= form.cleaned_data['add']
            css.image=form.cleaned_data['image']
            css.save()
            return redirect('/detail/'+ str(css.id))
    else:
        form = CSSForm(instance = css)
        return render(request, 'edit.html', {'css':css, 'form':form})

def review(request):
    if request.method == 'POST': 
        cform = CSSForm(request.POST, request.FILES)
        if cform.is_valid():
            cform.save() 
        return redirect('home')
    else:         
        form = CSSForm()
        return render(request, 'review.html',{'form': form} )

def update(request,css_id):
    edit_css = get_object_or_404(CSS, pk=css_id)
    # edit_css.title = request.POST['title']
    # edit_css.body = request.POST['body']
    # edit_css.pub_date = timezone.datetime.now()
    edit_css.title= request.POST['title'] 
    edit_css.area= request.POST['area']
    edit_css.time= request.POST['time']
    edit_css.mood= request.POST['mood']
    edit_css.floor= request.POST['floor']
    edit_css.toilet= request.POST['toilet']
    edit_css.smoke= request.POST['smoke']
    edit_css.elevator= request.POST['elevator']
    edit_css.pet= request.POST['pet']
    edit_css.add= request.POST['add']
    edit_css.image= request.POST['image']
    edit_css.save()
    return redirect('/detail/' + str(edit_css.id))

#def userinfo(request, username, password, nickname, school, phone_number):
#    CustomModel(username=username, password=password, nickname=nickname, school=school, phone_number=phone_number)
#    return render(request, 'css/mypage.html')

def delete(request, css_id):
    delete_css = get_object_or_404(CSS, pk=css_id)
    delete_css.delete()
    return redirect('home')

