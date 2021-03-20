from django.shortcuts import render
from Chittoor.models import Reg
from django.http import HttpResponse
# Create your views here.

def home(req):
	return render(req,'ctr/home.html')

def about(req):
	return render(req,'ctr/about.html')

def contact(request):
	return render(request,'ctr/contact.html')

def signup(request):
	if request.method == "POST":
		u = request.POST['uname']
		p = request.POST['pwd']
		# print(u,p)
		r = Reg(usname=u,psd=p)
		r.save()
		return HttpResponse("User Created Successfully")
	return render(request,'ctr/register.html')

def display(request):
	d = Reg.objects.all()
	return render(request,'ctr/display.html',{'p':d})