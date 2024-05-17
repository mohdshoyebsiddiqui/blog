
from django.shortcuts import render,redirect
from .models import Article
from .forms import UserCreate
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.hashers import make_password



# Create your views here.
def index(request):
    if User.is_authenticated:        
        data=Article.objects.all()
        usern=request.session.get('user_name')
    
        return render(request , 'index.html' ,{'data':data,'usern':'usern2'})
    else:
        return render(request , 'index.html' ,{'data':'','usern':'error'})


def article(request,id):
    if User.is_authenticated: 
        data=Article.objects.get(id=id)
        return render(request , 'article.html',{'data':data} )  
    else:
         return render(request , 'article.html',{'data':data} )
        



def signup(request):
    if request.method=='POST':
        fm=UserCreate(request.POST)
        if fm.is_valid():
            username=fm.cleaned_data['username']
            first_name=fm.cleaned_data['first_name']
            last_name=fm.cleaned_data['last_name']
            email=fm.cleaned_data['email']
            password=fm.cleaned_data['password2']
            saved=User(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
            saved.save()
            login(request, saved)
            return redirect('index')

    else:
        fm=UserCreate()


    return render(request , 'signup.html' ,{'fm':fm})

def logins(request):
    if  request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user= authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user )
            request.session['user2'] = username
            
        return redirect('index')
    else:

        return render(request, 'login.html',{'err':'ered'})
        


def logouts(request):
        logout(request)
        return redirect('index')


def search(request):
    if User.is_authenticated:  
        if request.method=='GET':
            data=[]
            sear=request.GET.get('search')
            data=Article.objects.filter(title__icontains=sear)

            return render(request,'search.html',{'data':data,'search':sear} )
    else:
        return render(request,'search.html',{'data':'','search':''} )


def video(request,id):
    if User.is_authenticated: 
        data=Article.objects.get(id=id)
        return render(request , 'video.html',{'data':data} )  
    else:
         return render(request , 'video.html',{'data':data} )

