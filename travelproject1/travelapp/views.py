from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Headss

# Create your views here.
def demo(request):
   obj=Place.objects.all()
   obj1 = Headss.objects.all()
   return render(request,"index.html",{'result':obj,'results':obj1})

