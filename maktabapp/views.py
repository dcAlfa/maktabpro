from django.shortcuts import render,redirect
from django.views import View
from news.models import *
from .models import *
from django.contrib.auth import logout,login, authenticate


class Index(View):
    def get(self,request):
        news = News.objects.filter().order_by('-id')[:3]
        return render(request, "index.html",{"news":news})
    def post(self,request):
        username = request.POST.get("u")
        password = request.POST.get("p")
        remember = request.POST.get('ch')
        if remember is None:
            user = authenticate(request, username=username,password=password)
        else:
            user = authenticate(request, username=username, password=password, remember=remember)

        if user is None:
            context = {"error":"Invalid username or password."}
            return render(request,"Index.html",context)
        login(request,user)
        return redirect("index")


class New(View):
    def get(self,request):
        news = News.objects.filter().order_by('-id')[:6]
        return render(request, "news.html",{"news":news})

class Media(View):
    def get(self,request):
        media = Alboom.objects.all()
        return render(request, "media.html",{"media":media})

class Jurnal(View):
    def get(self,request):
        if request.user.is_authenticated:
            sinf = Sinf.objects.filter(nomi="Green")
            sinff = Sinf.objects.filter(nomi="Blue")
            ac = Account.objects.get(user=request.user)
            oqtuvchi = Oqtuvchi.objects.get(account=ac)
            return render(request, "journal.html",{"sinf":sinff,"sinflar":sinf,"oqtuvchi":oqtuvchi})
        return redirect("index")




class Room(View):
    def get(self,request):
        if request.user.is_authenticated:
            return render(request, "Room.html")
        return redirect("index")

class Puplis(View):
    def get(self,request):
        if request.user.is_authenticated:
            return render(request, "puplis.html")
        return redirect("index")

class Jurnalitem(View):
    def get(self,request,pk):

        if request.user.is_authenticated:
            sinf = Sinf.objects.get(id=pk)
            ac = Account.objects.get(user=request.user)
            oqtuvchi = Oqtuvchi.objects.get(account=ac)
            oquvchilar = Oquvchi.objects.filter(sinf=sinf)
            chorak = Chorak.objects.filter()
            data = {
                "sinf": sinf,
                "chorak": chorak,
                "oqtuvchi": oqtuvchi,
                "oquvchi": oquvchilar,
            }

            return render(request, "journalItems.html",data)
        return redirect("index")
    def post(self,request,pk):
        ac = Account.objects.get(user=request.user)
        print(request.POST.get('ch1'))
        ch1 = request.POST['ch1']
        ch2 = request.POST.get("ch2")
        print(ch1)
        ch3 = request.POST.get("ch3")
        ch4 = request.POST.get("ch4")
        # Chorak(
        #         oquvchi="Muhammadali Muhammadjonov",
        #         oqtuvchi=oqtuvchi,
        #         baho1=ch1,
        #         baho2=ch2,
        #         baho3=ch3,
        #         baho4=ch4,
        #     ).save()
        # return redirect("index")
        return redirect("/juritem/3/")


class Contact(View):
    def get(self,request):
        return render(request, "Contact.html")


class Logout(View):
    def get(self,request):
        logout(request)
        return redirect("index")
