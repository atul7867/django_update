from django.shortcuts import render,HttpResponse
from .models import Facilitys,Role,Dept
from django.db.models import Q
# Create your views here.
def index(request):
    # return HttpResponse("welcome to our django website")
    return render(request,"home.html")

def add(request):
    if request.method=="POST":
        fname=request.POST["fname"]
        lname=request.POST["lname"]
        salary=int(request.POST["salary"])
        role=int(request.POST["role"])
        dept=int(request.POST["role"])
        phoneno=request.POST["phoneno"]
        new_fac=Facilitys(fname=fname,lname=lname,salary=salary,role_id=role,dept_id=dept,phoneno=phoneno)
        new_fac.save();
        return HttpResponse("successfully storedd data..")
    elif request.method=="GET":
        return render(request,"add.html")   
    else:
        return HttpResponse("somthing error")
    
def show(request):
    facs=Facilitys.objects.all()
    context={
        "facs":facs
    }
    print(facs)
    return render(request,"show.html",context)


def rem(request,fac_id=0):
    if fac_id:
        try:
            newkey=Facilitys.objects.get(id=fac_id)
            newkey.delete()
            return HttpResponse("delete succesfully")
        except:
            return HttpResponse("error")
    facs=Facilitys.objects.all()
    context={
        "facs":facs
    }
    return render(request,"rem.html",context)


def ser(request):
    if request.method=="POST":
        name=request.POST["fname"]
        role=request.POST["role"]
        facs=Facilitys.objects.all()
        if name:
            facs=facs.filter(fname__icontains=name)
        if role:
            facs=facs.filter(role_id__icontains=role)
        context={
            "facs":facs
        }
        return render(request,"show.html",context)
    elif request.method=="GET":
            return render(request,"ser.html")
    else:
        return HttpResponse("error")

    
def up(request):
    if request.method == "POST":
        fac_id = request.POST["fac_id"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        salary = int(request.POST["salary"])
        role_id = int(request.POST["role"])
        dept_id = int(request.POST["dept"])
        phoneno = request.POST["phoneno"]

        try:
            facility = Facilitys.objects.get(id=fac_id)
            facility.fname = fname
            facility.lname = lname
            facility.salary = salary
            facility.role_id = role_id
            facility.dept_id = dept_id
            facility.phoneno = phoneno
            facility.save()
            return HttpResponse("Facility updated successfully.")
        except Facilitys.DoesNotExist:
            return HttpResponse("Facility does not exist.")
    else:
        return render(request, "up.html")
    
