from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(request):
    peoples = [
        {"name":"Abhijeet","age": 12},
        {"name":"Dipanshu","age": 32},
        {"name":"sandeep","age": 23},
        {"name":"Aaru","age": 67}
    
   ]
    for people in peoples:
        if people ["age"]:
            print("Yes")
    vegetables = ["Pumpkin", "Tomato", "Potato"]
    
    return render(request, "index.html",context={"page":"Django 2023 Tutorial","peoples" : peoples,"vegetables":vegetables})
def about(request):
    context = {"page" : "About"}
    return render(request, "about.html")

def contact(request):
    context = {"page" : "Contact"}
    return render(request, "contact.html",context)

    