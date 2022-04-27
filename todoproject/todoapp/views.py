from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from . models import *
import easygui

# Create your views here.
def login(request):
    if request.method=='POST':
        if Todosign.objects.filter(user_name=request.POST['user_name'],password=request.POST['password']).exists():
            usersign=Todosign.objects.filter(user_name=request.POST['user_name'],password=request.POST['password'])
            easygui.msgbox("Welcome")
            return render(request,'dashboard.html',{'usersign':usersign})
        else:
            context={'msg':"wrong credential"}  
            return render(request,'login.html',context)  
    return render(request,'login.html')

def sign(request):
    if request.method=="POST":
        if Todosign.objects.filter(email_id=request.POST['email_id']):
            easygui.msgbox("Mail already taken")
        else:
            usersign=Todosign()
            usersign.user_name=request.POST['user_name']
            usersign.password=request.POST['password']
            usersign.email_id=request.POST['email_id']
            usersign.save()
            easygui.msgbox("success")
            return redirect(login)
    return render(request,'sign.html')

def dashboard(request):
    mytask=usertask.objects.all()
    if request.method=="POST":
        mytask=usertask()
        mytask.tasks=request.POST['tasks']
        mytask.percentages=request.POST['percentages']
        mytask.dates=request.POST['dates']
        mytask.save()
        easygui.msgbox("Task added")
        return redirect(dashboard)
    return render(request,'dashboard.html',{'mytask':mytask})    

def update(request,id):
    edit=usertask.objects.get(id=id)
    return render(request,'update.html',{'edit':edit}) 

def updateedit(request,id):
    tasks=request.POST['tasks']
    percentages=request.POST['percentages']
    dates=request.POST['dates']
    edit=usertask.objects.all().filter(id=id).update(tasks=tasks,percentages=percentages,dates=dates)
    easygui.msgbox("Updated")
    return redirect(dashboard)

def delete(request,id):
    deletes=usertask.objects.all().get(id=id)
    deletes.delete()
    return redirect(dashboard)  

def logout(request):
    if request.session.has_key('id'):
        del request.session['id']
        logout(request)
        return redirect(login)