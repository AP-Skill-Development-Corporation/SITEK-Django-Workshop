from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(req):
	return render(req,"std/home.html")

def about(req):
	return render(req,"std/about.html")

def html(rt):
	return HttpResponse("<h1 style='background-color:green'>Welcome <i>Raju</i></h1><h3>This is sample</h3>")

def sgprt(re,n):
	return HttpResponse("<h1> Hi Welcome <span style='color:green'>"+n+"</span></h1>")

def twprt(req,nm,ag):
	return HttpResponse("<h2>Your Name is: <span style='color:magenta'>"+nm+"</span></h2><h3>Your age is: <span style='color:yellow'>"+str(ag)+"</span></h3>")

def regis(request):
	if request.method == "POST":
		username = request.POST['uname']
		pwd = request.POST['pd']
		# print(username,pwd)
		return render(request,"std/display.html",{'u':username})
	return render(request,"std/rg.html")

