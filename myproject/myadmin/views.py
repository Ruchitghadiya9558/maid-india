from django.shortcuts import render


def homepage(request):
	return render(request,'myadmin/dashbord.html')

def addstate(request):
	return render(request,'myadmin/add_State.html')

def allstate(request):
	return render(request,'myadmin/all_state.html')	

def addcity(request):
	return render(request,'myadmin/add_city.html')

def allcity(request):
	return render(request,'myadmin/all_city.html')

def allinquity(request):
	return render(request,'myadmin/all_inquiry.html')

def allcustomer(request):
	return render(request,'myadmin/all_customer.html')

def allmaidapplication(request):
	return render(request,'myadmin/all_maid_application.html')

def dashbord(request):
	return render(request,'myadmin/dashbord.html')	