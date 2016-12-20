from django.shortcuts import render, redirect
from .models import Pet, PetManager
# # Create your views here.
def users(request):
    if request.method == "POST":
        return create(request)
    #Else it's a GET, send to index method to return html
    return index(request)
#
def users_w_id(request, id):
    if request.method == "POST":
        return update(request, id)
    return show(request, id)


def index(request):
    #Logic
    context = {
        "pets": Pet.objects.all(),
    }
    return render(request, "semirestful/index.html", context)

def create(request):
    Pet.objects.create(name=request.POST["name"], description=request.POST["description"], type_of_pet=request.POST["type_of_pet"], breed=request.POST["breed"])
    return redirect("/pets")

def new(request):
    return render(request, "semirestful/new.html")

def show(request, id):
    pet = Pet.objects.get(id=id)
    return render(request, "semirestful/show.html", { "pet": pet })

def edit(request, id):
    pet = Pet.objects.get(id=id)
    return render(request, "semirestful/edit_pet.html", { "pet": pet })

def update(request, id):
    #Outsource to Models Manager
    Pet.objects.update(id, request.POST)
    # Pet.objects.update(id)
    return redirect("/pets")

def destroy(request, id):
    Pet.objects.get(id=id).delete()
    return redirect("/pets")
