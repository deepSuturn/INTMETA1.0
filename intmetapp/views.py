from collections import Counter

from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
import os

from django.contrib import messages
import os
import json
from intmeta.intmetapp import core

# Create your views here.


#dict ={}
def index(request):

    context = {}
    global attribute, dfd3, maxpercent


    if request.method == 'POST':

        uploaded_file = request.FILES['document']
        attribute = request.POST.get('attributeid')

        print(attribute)

        savefile = FileSystemStorage()
        name = savefile.save(uploaded_file.name, uploaded_file) #gets the name of the file

        d = os.getcwd() # how we get the current directory
        file_directory = d+'/media/'+name #saving the file in the media directory
        with open(file_directory) as f:
            identify = f.readline()
            print(identify)
            if 'unclassified' in identify:
                print("kraken file")
                dfd3, maxpercent = core.kraken(file_directory, attribute)

                return redirect(results)
            elif 'Proportion_Classified(%)' in identify:
                print("clarkfile")
                dfd3, maxpercent = core.clark(file_directory, attribute)
                return redirect(results)
            elif 'abundance' in identify:
                print("metamaps file")
                dfd3, maxpercent = core.metamaps(file_directory, attribute)
                return redirect(results)  
        request.session['attribute'] = attribute

    return render(request, 'index.html', context)


#project_data.csv
    
def results(request):
    dfd3_json = json.dumps(dfd3, indent = 4, default=str, ensure_ascii=False)
    return render(request, 'results.html', {'dfd3_json':dfd3_json, 'maxpercent':maxpercent})

def krona(request):
    return render(request, 'krona.html')
