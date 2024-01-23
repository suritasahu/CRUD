from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import Msg

# Create your views here.

def create(request):
    # print("request =",request.method)
    if request.method =="GET":
        print("we are in get method")
        return render(request,"create.html")
    else:
        print("we are in POST")

        # fetching data
        nm=request.POST["uname"]
        print(nm)
        
        em=request.POST["uemail"]
        print(em)

        mb=request.POST["umobile"]
        print(mb)

        ms=request.POST["msg"]
        print(ms)

        m= Msg.objects.create(name=nm, email=em,mobile=mb,massage=ms)
        print(m)
        return HttpResponse("datasaved")
    
def show(request):
    m=Msg.objects.all()
    print(m)
    context={}
    context["data"]=m 
    return render(request,"dashboard.html",context)

def delete(request,rid): 
    # print("deleted id", rid)
    m=Msg.objects.filter(id=rid)
    m.delete()

    # for i in m:
    #     print(i.name)
    #     print(i.email)
    #     print(i.mobile)
    return HttpResponse("deleted id is "+rid)

def edit(request,rid):
    if request.method=="GET":

        m=Msg.objects.filter(id=rid)
        context={}
        context["data"]=m
        return render(request,"edit.html",context)
    else:
        
        nm=request.POST["uname"]
        # print(nm)
        
        em=request.POST["uemail"]
        # print(em)

        mb=request.POST["umobile"]
        # print(mb)

        ms=request.POST["msg"]
        # print(ms)

        m=Msg.objects.filter(id=rid)
        m.update(name=nm, email=em,mobile=mb,massage=ms)
        return redirect("/dash")
    
        


        
        

       




