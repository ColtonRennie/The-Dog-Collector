from django.shortcuts import render
from django.http import HttpResponse

class Dog:  
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

dogs = [
  Dog('Norah', 'Belgian Tervuren', 'She is a long haired mixed tans and black that has a lot of energy', 8),
  Dog('Youki', 'Mixed', 'He is starting to get lazy in his old age, but is always up for a fight', 9),
  Dog('Sadie', 'Mixed', 'She is the youngest of the pack and with lots of spunk and personality', 3)
]

def home(request):
  return render(request,'base.html')

def about(request):
  return render(request, 'about.html')

def dogs_index(request):
  return render(request, 'dogs/index.html', { 'dogs': dogs })

