from django.http import HttpResponse
from django.shortcuts import render
from .models import Place
from .models import Team
# Create your views here.
def demo(request):
   obj=Place.objects.all()
   key = Team.objects.all()
   return  render(request,"index.html",{'result':obj,'pen':key})

#
# def gang(request):
#    key=Team.objects.all()
#    return  render(request,"index.html",{'pen':key})
# def about(request):
#    return  render(request,"about.html")
