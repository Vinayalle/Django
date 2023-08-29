from django.shortcuts import render
from django.http import HttpResponse
from .models import Tasks
# Create your views here.
def hello_world(request):
    return HttpResponse("hello vinay")
def home_page(request):
    return render(request,"index.html")
def task(request):
    task1=Tasks()
    task1.task_name='website design'
    task1.assigned_to='vinayalle'
    return render(request,"task.html",{'task1':task1})