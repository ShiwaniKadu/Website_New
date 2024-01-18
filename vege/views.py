from django.shortcuts import render,redirect
from . models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.core.paginator import Paginator
from django.db.models import Q,Sum
# from django.contrib.auth import login_required

# @login_required(login_url="/login/")
# Create your views here.
def receipes(request):
    if request.method == "POST":

        data = request.POST
        receipe_image = request.FILES.get("receipe_image")
        receipe_name = data.get("receipe_name")
        receipe_description = data.get("receipe_description")

        Receipe.objects.create(
            receipe_image=receipe_image,
            receipe_name=receipe_name,
            receipe_description=receipe_description
            )
        return redirect("/")
    
    queryset = Receipe.objects.all()

    if request.GET.get("search"):
        queryset=queryset.filter(receipe_name__icontains = request.GET.get("search"))
    context = {"receipes": queryset}
        
    return render(request, "receipes.html",context)
# @login_required(login_url="/login/")
def delete_receipe(request, id):
    queryset = Receipe.objects.get(id=id)
    queryset.delete()
    return redirect("/")

# @login_required(login_url="/login/")
def update_receipe(request, id):
    queryset = Receipe.objects.get(id=id)
    if request.method == "POST":
        data = request.POST

        receipe_image = request.FILES.get("receipe_image")
        receipe_name = data.get("receipe_name")
        receipe_description = data.get("receipe_description")

        queryset.receipe_name=receipe_name
        queryset.receipe_description=receipe_description  

        if receipe_image:
            queryset.receipe_image=receipe_image
            queryset.save() 
            return redirect("/")
   
    context = {"receipe": queryset}

    return render(request, "update_receipes.html",context)

def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        passowrd = request.POST.get("password")

        if not User.objects.filter(username = username).exists():
            messages.error(request, "Invalid Username")
            return redirect("/login/")
        
        user = authenticate(username=username, passowrd=passowrd)

        if user is None:
            messages.error(request, "Invalid Password")
            return redirect("/login/")
        
        else:
            login(request, user)
            return redirect("/receipes/")


    return render(request, "login.html")

def logout_page(request):
    logout(request)
    return redirect("/login/")



def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        passowrd = request.POST.get("password")
        
        user= User.objects.filter(username = username)

        if user.exists():
            messages.info(request, "Username already exists")
            return redirect("/register/")
        
        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
        )

        user.set_password(passowrd)
        user.save()

        messages.info(request, "Account created successfully")

        return redirect('/register/')
    return render(request, "register.html")

def get_student(request):
    queryset = Student.objects.all()
    if request.GET.get("search"):
        search=request.GET.get("search")
        queryset=queryset.filter(
            Q(student_name__icontains=search) |
            Q(department_department__icontains=search) |
            Q(student_id_student_id__icontains=search) |
            Q(student_email__icontains=search) |
            Q(student_age__icontains=search)
        )
    paginator=Paginator(queryset,25)
    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    print(page_obj.object_list)
    return render(request,"students.html",{"queryset":page_obj})

def see_marks(request,student_id):
    queryset=SubjectsMarks.objects.filter(student__student_id__student_id=student_id)
    total_marks = queryset.aggregate(total_marks = Sum("marks"))
    print(total_marks)
    return render(request,"see_marks.html",{"queryset":queryset,"total_marks":total_marks})

