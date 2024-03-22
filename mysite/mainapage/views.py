from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect,get_object_or_404
from mainapage.models import ExtendedUser
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import update_session_auth_hash
from mainapage.models import*
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from django.contrib.auth.models import User,auth
from django.utils.html import strip_tags
from django.conf import settings
# Create your views here.
def indexpage(request):
    c=Cateogry.objects.all()
    t=Title.objects.all().first()
    c3=Content.objects.all().first()
    h=Headline.objects.all().first()
    wb=WebButton.objects.all().first()
    d=Webtext.objects.all().first()
    desti=destination.objects.all()
    latdes=latestdesti.objects.all()
    alldesti=alldestinationowl.objects.all()
    wimg=webimage.objects.all()
    popguide=popularguides.objects.all()
    traguide=Travelguides.objects.all()
    tourex=Experiences.objects.all()
    lapa=Lastpage.objects.all()
    lapaCon=lastpageContent.objects.all()
    return render(request,'index.html',{"c":c,"t":t,"c3":c3,"h":h,"wb":wb,"d":d,"desti":desti,
    "alldesti":alldesti,"wimg":wimg,"latdes":latdes,"popguide":popguide,"traguide":traguide,"tourex":tourex,"lapa":lapa,"lapaCon":lapaCon})

def login(request):
    if request.method=='POST':
            uname=request.POST['username']
            ppass=request.POST['uspass']
            print(uname,ppass)
            user=auth.authenticate(username=uname,password=ppass)
            if user is not None:
                auth.login(request,user)
                # myproducts=Product.objects.all()
                if request.user.is_authenticated:
                   return HttpResponseRedirect('/')
                return render(request,'index.html')
               
            else:
                print("record not found") 
                messages.info(request,'Password or username is incorrect Or Create your new Account')  
                return redirect('login')
                # this elif is for get request
    # elif request.user.is_authenticated:
        # myproducts=Product.objects.all()
        # profile = ExtendedUser.objects.get(user=request.user)
        # return render(request,'index.html',{'profile':profile,'myproducts':myproducts})
    return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
def profile(request):
    c=Cateogry.objects.all()
    wimg=webimage.objects.all()
    t=Title.objects.all().first()
    ob=blogdesti.objects.all()    
    wimg=webimage.objects.all()
    aw=Aboutwho.objects.all()
    lapa=Lastpage.objects.all()
    lapaCon=lastpageContent.objects.all()
     
    if request.user.is_authenticated:
        profile = ExtendedUser.objects.get(user=request.user)
        print(profile)
        return render(request,'profile.html',{'profile':profile,"c":c,"t":t,"wimg":wimg,"ob":ob,"wimg":wimg,"lapa":lapa,"lapaCon":lapaCon,"aw":aw})
def signup(request):
    if request.method=='POST':
        f_name=request.POST['firstname']
        l_name=request.POST['lastname']
        u_name=request.POST['username']
        passw2=request.POST['repassword']
        email=request.POST['email']
        phone1=request.POST['phone']
        phone2=request.POST['altnum']
        addre=request.POST['address']
        print(f_name)
        if User.objects.filter(username=u_name).exists():
            messages.info(request,'User Name already exists...')
            print("user pale se available hai")
            return redirect('signup')
        else:
            user=ExtendedUser.objects.create_user(first_name=f_name,last_name=l_name,username=u_name,password=passw2,email=email,phone_no=phone1, alt_no=phone2,address=addre)
            user.save()
            user=auth.authenticate(username=u_name,password=passw2)
            if user is not None:
                auth.login(request,user)
                return HttpResponseRedirect('/')
            return redirect('signin')     
                # messages.add_message(request,messages.SUCCESS,' Account Created Successfully..!!!')
            # print("user created") 
    return render(request,'signup.html')
def edit(request):
    return render(request,'edit.html')
def blog(request):
    lapa=Lastpage.objects.all()
    lapaCon=lastpageContent.objects.all()
    c=Cateogry.objects.all()
    t=Title.objects.all().first()
    ob=blogdesti.objects.all()
    wimg=webimage.objects.all()
    entries_per_page = 6
    paginator = Paginator(ob, entries_per_page)

    page = request.GET.get('page')
    try:
        ob = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        ob = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver last page of results.
        ob = paginator.page(paginator.num_pages)
        
    return render(request,"blog.html",{"ob":ob,"c":c,"t":t,"lapa":lapa,"lapaCon":lapaCon,"wimg":wimg})

def explore(request):
    lapa=Lastpage.objects.all()
    lapaCon=lastpageContent.objects.all()
    c=Cateogry.objects.all()
    t=Title.objects.all().first()
    ob=blogdesti.objects.all()    
    wimg=webimage.objects.all()
    entries_per_page = 6
    paginator = Paginator(ob, entries_per_page)

    page = request.GET.get('page')
    try:
        ob = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        ob = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver last page of results.
        ob = paginator.page(paginator.num_pages)
        
    return render(request,"explore.html",{"ob":ob,"c":c,"t":t,"lapa":lapa,"lapaCon":lapaCon,"wimg":wimg})

def destinationtour(request):
    c=Cateogry.objects.all()
    wimg=webimage.objects.all()
    t=Title.objects.all().first()
    ob=blogdesti.objects.all()    
    wimg=webimage.objects.all()
    lapa=Lastpage.objects.all()
    lapaCon=lastpageContent.objects.all()
    return render(request,'destinationtour.html',{"c":c,"t":t,"wimg":wimg,"ob":ob,"wimg":wimg,"lapa":lapa,"lapaCon":lapaCon})
def about(request):
    c=Cateogry.objects.all()
    wimg=webimage.objects.all()
    t=Title.objects.all().first()
    ob=blogdesti.objects.all()    
    wimg=webimage.objects.all()
    aw=Aboutwho.objects.all()
    lapa=Lastpage.objects.all()
    lapaCon=lastpageContent.objects.all()
    return render(request,'about.html',{"c":c,"t":t,"wimg":wimg,"ob":ob,"wimg":wimg,"aw":aw,"lapa":lapa,"lapaCon":lapaCon})
def readmore(request,myid):
    c=Cateogry.objects.all()
    wimg=webimage.objects.all()
    t=Title.objects.all().first()
    ob=blogdesti.objects.all()    
    wimg=webimage.objects.all()
    aw=Aboutwho.objects.all()
    lapa=Lastpage.objects.all()
    lapaCon=lastpageContent.objects.all()
    x=blogdesti.objects.filter(id=myid).first()
    return render(request,'readmore.html',{"x":x,"c":c,"t":t,"wimg":wimg,"ob":ob,"wimg":wimg,"aw":aw,"lapa":lapa,"lapaCon":lapaCon})
def search(request):
    c=Cateogry.objects.all()
    wimg=webimage.objects.all()
    t=Title.objects.all().first()

    if "qry" in request.GET:
        
        q=request.GET["qry"]
        print(q)
        if blogdesti.objects.filter(a__icontains=q):
            myquery=blogdesti.objects.filter(a__icontains=q)
            print(myquery)
            return render(request,"search.html",{"myquery":myquery,"c":c,"t":t,"wimg":wimg})
        elif blogdesti.objects.filter(id__icontains=q):
            myquery=blogdesti.objects.filter(id__icontains=q)
            return render(request,"search.html",{"myquery":myquery,"c":c,"t":t,"wimg":wimg})
        else:
             return HttpResponse("<h1>No result found</h1>")
    else:
        return HttpResponse("<h1>No result found</h1>")
