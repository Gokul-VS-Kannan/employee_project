from django.shortcuts import render,redirect
from.models import Employee
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.
@login_required
def home(request):
    return render(request,'index.html')

def loginview(request):
    uname = request.POST['username']
    pwd = request.POST['password']
    user = authenticate(request,username=uname,password=pwd)
    if user is not None:
        login(request,user)
        return redirect('home')
    else:
        return render(request,"login.html",{"msg":"Invalid login"})

def logout_view(request):
    logout(request)
    return redirect('login')

def sign_up(request):
    try:
        form = UserCreationForm(request.POST)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect('login')
        else:
            return render(request,'sign_up.html',{'form': userform,'msg':'Invalid Login'})
    except Exception as e:
        print(e)
        userform = UserCreationForm()
        return render(request,'sign_up.html',{'form':userform})

@login_required
def addemployee(request):
    Name=request.POST['name']
    Address=request.POST['address']
    Age=request.POST['age']
    PhoneNumber=request.POST['phoneno']
    # we create an object of class Product with atributes given in the table and it's value coresponds to the value we enter in html form
    empobj=Employee(name=Name,address=Address,age=Age,phoneno=PhoneNumber)
    #.save()function will save the data in table
    empobj.save()
    return render(request,"index.html",{"msg":"Employee added"})

def display(request):
    empdtls=Employee.objects.all()
    return render(request,"index.html",{'emp':empdtls})

'''
#read operation
Employee.objectts.all()                 :-fetch all records
Employee.objects.filter(name="abc")     :-fetch multiple records using same condition 
Employee.objects.get(id=1)              :-fetch only a single record
Employee.objects.order_by('name')[:5]   :-fetch first 5 employee by name
Employee,objects.value('name').annotate(count=Count('id')) :-fetches the count of value name
'''
@login_required
def delemployee(request):
    empname=request.POST['name']
    empdtls=Employee.objects.filter(name=empname)
    empdtls.delete()
    return render(request,"index.html",{"msg":"Deleted"})

@login_required
def updatename(request):
    try:
        oldname = request.POST["oldname"]
        newname = request.POST["newname"]
        emp = Employee.objects.filter(name=oldname)
        if emp.exists():
            emp.update(name=newname)
            return render(request,"index.html",{"msg":"Update employee's name"})
        else:
            return render(request,"index.html",{"msg":"No record found"})
    except Exception as e:
        print(e)
        return render(request,"index.html",{"msg":"Not Updated"})
