from django.shortcuts import render
from django.http import HttpResponseRedirect
import csv
import pandas as pd
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os
import cv2
import numpy as np


# Create your views here.

def strona_glowna(request):
    return render(request, 'strona_glowna.html', {})

def about(request):
    return render(request, 'about.html', {})

adresy=[]
def porownac(path1, path2):
    global adresy
    original = cv2.imread(path1, 1)
    duplicate = cv2.imread(path2, 1)
    # 1) Check if 2 images are equals
    if original.shape == duplicate.shape:
        print("The images have same size and channels")
        difference = cv2.subtract(original, duplicate)
        b, g, r = cv2.split(difference)


        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
            return 1
        else:
            return 0


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        print("APPENDUJE1:",uploaded_file_url)
        adresy.append(str(uploaded_file_url))
        return render(request, 'simple_upload.html', {'uploaded_file_url': uploaded_file_url})
    return render(request, 'simple_upload.html')

def simple_upload2(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        print("APPENDUJE2:",str(uploaded_file_url))
        adresy.append(str(uploaded_file_url))
        print(adresy)

        return render(request, 'simple_upload2.html', {'uploaded_file_url': uploaded_file_url})
    return render(request, 'simple_upload2.html')


def porownaj(request):
        #print("JAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",adresy[-1], adresy[-2])
        if porownac(adresy[-1][1:],adresy[-2][1:])==1:
            info="Obrazki są takie same."
        else:
            info="Obrazki są różne."

        return render(request, 'porownaj.html', {"info":info})
