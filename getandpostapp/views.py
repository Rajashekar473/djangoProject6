from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.
class getinput(View):
    def get(self,request):
        return render(request,'input.html')
class postinput(View):
    def get(self,request):
        return render(request,'output.html')
class add(View):
    def get(self,request):
        x=request.GET["t1"]
        y=request.GET["t2"]
        i=int(x)
        j=int(y)
        k=i+j
        return HttpResponse("The sum is:" +str(k))
    def post(self,request):
        x=request.POST["t1"]
        y=request.POST["t2"]
        i=int(x)
        j=int(y)
        z=i+j
        return HttpResponse("The sum is:" +str(z))