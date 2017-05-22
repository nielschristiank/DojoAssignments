# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'disappearingNinja/index.html')

def ninjas(request):
    ninja_dict = {
        'ninja_color': "green",
        'ninja_name': "Teenage Mutant Ninja Turtles",
        'ninja_src': "disappearingNinja/img/tmnt.png"
    }
    return render(request, 'disappearingNinja/ninjas.html', ninja_dict)

def ninja_color(request, ninja_color):

    if ninja_color == "blue":
        src = "disappearingNinja/img/leonardo.jpg"
        ninja_name = "Leonardo"
    elif ninja_color == "red":
        src = "disappearingNinja/img/raphael.jpg"
        ninja_name = "Raphael"
    elif ninja_color == "orange":
        src = "disappearingNinja/img/michelangelo.jpg"
        ninja_name = "Michelangelo"
    elif ninja_color == "purple":
        src = "disappearingNinja/img/donatello.jpg"
        ninja_name = "Donatello"
    else:
        src = "disappearingNinja/img/notapril.jpg"
        ninja_name = "Not a Turtle"

    ninja_dict = {
        'ninja_color': ninja_color,
        'ninja_name': ninja_name,
        'ninja_src': src
    }
    return render(request, 'disappearingNinja/ninjas.html', ninja_dict)
