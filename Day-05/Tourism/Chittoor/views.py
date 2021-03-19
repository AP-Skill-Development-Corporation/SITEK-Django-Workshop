from django.shortcuts import render

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
		print(u,p)
	return render(request,'ctr/register.html')