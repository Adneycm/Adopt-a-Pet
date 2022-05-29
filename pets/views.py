from django.shortcuts import render, redirect
from django.http import Http404
from .models import Pet
from .requisicoes import *


def index(request):
    return render(request, 'pets/index.html', {'pets': get_default_animals()})


def adoptPage(request):
    id = request.POST.get('id')
    print(f"id############# = {id}")
    name, type, age, genre, size, description, img = get_pet_byID(id)
    print(f"name = {name}")
    print(f"type = {type}")
    print(f"age = {age}")
    print(f"genre = {genre}")
    print(f"size = {size}")
    print(f"description = {description}")
    print(f"img = {img}")
    pet = Pet(id, name, type, age, genre, size, description, img)
    pet.save()
    return redirect('index')

def wantoAdopt(request):
    all_pets = Pet.objects.all()
    return render(request, 'pets/wantoAdopt.html', {'pets': all_pets}) 

