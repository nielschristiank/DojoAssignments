# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
import math


# Create your views here.
def index(request):
    return render(request, 'landscapes/index.html')

# def result(request):
#     return render(request, 'landscapes/result.html')

def landscape(request, num):
    print num
    n = int(num)
    print n
    if n > 0 and n < 51:
        n = int(math.ceil(n/10.0))
        print n
    else:
        n = 18
    img_src = {
        'src': "landscapes/img/"+str(n)+".jpg"
    }
    print img_src['src']
    return render(request, 'landscapes/landscape.html', img_src)



    # if n > 0 and n < 11:
    #     pass
    # elif n > 10 and < 21:
    #     pass
    # elif n > 20 and n < 31:
    #     pass
    # elif n > 20 and n < 31:
    #     pass
    # elif
