from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
import os
import os
import json
from intmeta.intmetapp import core
from intmeta.intmetapp import subcalls

# Create your views here.

def index(request):

    context = {}
    global attribute, dfd3, maxpercent


    if request.method == 'POST':

        uploaded_file = request.FILES['document']
        attribute = request.POST.get('attributeid')

        print(attribute)

        savefile = FileSystemStorage()
        name = savefile.save(uploaded_file.name, uploaded_file) # pega o nome do arquivo

        d = os.getcwd() # how we get the current directory
        file_directory = d+'/media/'+name #saving the file in the media directory
        with open(file_directory) as f:
            # Aqui ele identifica qual é o tipo de arquivo, se é Kraken, Clark, Metamaps, etc...
            identify = f.readline()
            if 'unclassified' in identify:
                print("kraken file")
                dfd3, maxpercent = core.kraken(file_directory, attribute)                
                subcalls.krakenkrona(file_directory)
                return redirect(results)
            elif 'Proportion_Classified(%)' in identify:
                print("clarkfile")
                dfd3, maxpercent = core.clark(file_directory, attribute)
                subcalls.clarkkrona(file_directory)
                return redirect(results)
            elif 'abundance' in identify:
                print("metamaps file")
                dfd3, maxpercent = core.metamaps(file_directory, attribute)
                return redirect(results)  
        request.session['attribute'] = attribute

    return render(request, 'index.html', context)


def results(request):
    # O arquivo volta do parse já convertido para dicionário
    # Agora nós convertemos o dicionário para JSON
    dfd3_json = json.dumps(dfd3, indent = 4, default=str, ensure_ascii=False)
    return render(request, 'results.html', {'dfd3_json':dfd3_json, 'maxpercent':maxpercent})


def krona(request):
    return render(request, 'krona.html')
