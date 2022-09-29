from django.shortcuts import render
from django.http import HttpResponse

class Dog:  
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

dogs = [
  Dog('Barky', 'Mixed', 'bad dog', 3),
  Dog('Dancer', 'Mixed', 'good dog', 6),
  Dog('Rudolph', 'Mixed', 'This is a dog', 5)
]

def home(request):
  return render(request,'base.html')

def about(request):
  return render(request, 'about.html')

def dogs_index(request):
  return render(request, 'dogs/index.html', { 'dogs': dogs })

