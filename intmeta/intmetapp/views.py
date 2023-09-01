from html.entities import name2codepoint
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
import os
import json
from intmeta.intmetapp import core
from intmeta.intmetapp import subcalls
import datetime
import pandas as pd

# Create your views here.


def index(request):
    request.session.clear()
    return render(request, 'index.html')


def kraken(request, uploaded_file2=None):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        attribute = request.POST.get('attributeid')
        savefile = FileSystemStorage()
        # Pega o nome do arquivo
        name = savefile.save(uploaded_file.name, uploaded_file)
        # how we get the current directory
        d = os.getcwd()
        # saving the file in the media directory
        file_directory = d + '/media/' + name
        print("kraken file")
        # Tratamento de erro, modifica o comportamento a cada erro identificado
        try:
            dfd3, dfd3_2, maxpercent, maxreads, total_reads, most_classified_organism = core.kraken(file_directory, attribute)
            request.session['dfd3'] = dfd3
            request.session['dfd3_2'] = dfd3_2
            request.session['maxpercent'] = int(maxpercent)
            request.session['maxreads'] = int(maxreads)
            request.session['total_reads'] = int(total_reads)
            request.session['most_classified_organism'] = most_classified_organism
            request.session['twofiles'] = False
            request.session.save()
            if uploaded_file2 is not None:
                dfd32, dfd3_22, maxpercent2, maxreads2, total_reads2, most_classified_organism2 = core.kraken(file_directory, attribute)
                request.session['dfd32'] = dfd32
                request.session['twofiles'] = True
                request.session.save()
        except IndexError:
            return redirect(index)
        except ValueError:
            return redirect(index)
        subcalls.krakenkrona(file_directory)
        return redirect(results)
    return render(request, 'kraken.html')


def clark(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        savefile = FileSystemStorage()
        # pega o nome do arquivo
        name = savefile.save(uploaded_file.name, uploaded_file)
        uploaded_file2 = request.FILES['document2']
        savefile2 = FileSystemStorage()
        # pega o nome do arquivo
        name2 = savefile2.save(uploaded_file2.name, uploaded_file2)
        # how we get the current directory
        d = os.getcwd()
        # saving the file in the media directory
        file_directory = d + '/media/' + name
        # saving the file in the media directory
        file_directory2 = d + '/media/' + name2
        # Tratamento de erro, modifica o comportamento a cada erro identificado
        try:
            dfd3, dfd3_2, maxpercent, maxreads, total_reads = core.clark(file_directory)
            request.session['dfd3'] = dfd3
            request.session['dfd3_2'] = dfd3_2
            request.session['maxpercent'] = int(maxpercent)
            request.session['maxreads'] = int(maxreads)
            request.session['total_reads'] = int(total_reads)
            request.session.save()
        except IndexError:
            return redirect(index)
        except ValueError:
            return redirect(index)
        subcalls.clarkkrona(file_directory2)
        return redirect(results)
    return render(request, 'clark.html')


def metamaps(request):
    return render(request, 'metamaps.html')


def dc(request):
    request.session.clear()
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def krona(request):
    return render(request, 'krona.html')


def results(request):
    dfd3 = request.session['dfd3']
    dfd3_2 = request.session['dfd3_2']
    maxpercent = request.session['maxpercent']
    maxreads = request.session['maxreads']
    total_reads = request.session['total_reads']
    most_classified_organism = request.session['most_classified_organism']
    dfd3_json = json.dumps(dfd3, indent=4, default=str, ensure_ascii=False)
    dfd3_2 = json.dumps(dfd3_2, indent=4, default=str, ensure_ascii=False)
    print(dfd3_2)
    return render(request, 'results.html', {'dfd3_json': dfd3_json, 'dfd3_2': dfd3_2, 'maxreads': maxreads, 'total_reads': total_reads, 'maxpercent': maxpercent, 'most_classified_organism': most_classified_organism})
