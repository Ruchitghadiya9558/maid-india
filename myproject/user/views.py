from django.shortcuts import render


def homepage(request):
	return render(request,'user/index.html')

def aboutpage(request):
	return render(request,'user/aboutpage.html')

def contact(request):
	return render(request,'user/contact.html')

def postjob(request):
	return render(request,'user/post_job.html')

def registation(request):
	return render(request,'user/registation.html')

def login(request):
	return render(request,'user/login.html')

def maid(request):
	return render(request,'user/maid.html')	
	