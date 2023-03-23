from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def InsertPageView(request):
    return render(request,"app/insert.html")

def InsertData(request):
    #date come from html to view
    fname=request.POST['fname']
    lname=request.POST['lname']
    email=request.POST['email']
    contact=request.POST['contact']
    
    #creating object of Model Class
    #insert data to tables
    newuser=Student.objects.create(Firstname=fname,Lastname=lname,Email=email,Contact=contact)
    
    #after insert render on show.html
    # return render(request,"app/show.html")
    #after insery render on showpage view
    return redirect('showpage')

#show page view
def ShowPage(request):
    #select * from table
    all_data=Student.objects.all()
    return render(request,"app/show.html",{'key1':all_data})

    
#edit page view
def Editpage(request,pk):
    #fetching data of particular id
    get_data=Student.objects.get(id=pk)
    return render(request,"app/edit.html",{'key2':get_data})

# update Data view
def UpdateData(request,pk):
    udata=Student.objects.get(id=pk)
    udata.Firstname=request.POST['fname']
    udata.Lastname=request.POST['lname']
    udata.Email=request.POST['email']
    udata.Contact=request.POST['contact']
    #query for update
    udata.save()
    #render to show page
    return redirect('showpage')


#Delete Data view
def DeleteData(request,pk):
    ddata=Student.objects.get(id=pk)
    #query for deleting
    ddata.delete()
    return redirect('showpage')