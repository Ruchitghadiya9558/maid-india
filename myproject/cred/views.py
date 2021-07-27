from django.shortcuts import render
from cred.forms import CustomerFrom,ProductFrom
from cred.models import Customer

def Create(request):
	if request.method=='post':
		obj = CustomerFrom(request.POST)
		if obj.is_valid():
			obj.save()
	else:
		obj = CustomerFrom()

	context = {'form':obj}
	return render(request,'cred/insert.html',context)

def Create(request):
	if request.method=='post':
		obj = ProductFrom(request.POST)
		if obj.is_valid():
			obj.save()
	else:
		obj = ProductFrom()

	context = {'form':obj}
	return render(request,'cred/insert.html',context)

def read(request):
	result = Customer.objects.all()
	context = {'data':result}
	return render(request, 'cred/table.html',context)

def list(request):
	result = Customer.objects.all()
	context = {'data':result}
	return render(request, 'cred/list.html',context)

def drp(request):
	result = Customer.objects.all()
	context = {'data':result}
	return render(request, 'cred/drp.html',context)	


