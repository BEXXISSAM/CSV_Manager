import csv
import fileinput
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ImportFileForm
from .models import RIDModel, ImportFileModel
import datetime


def upload_file(request):
    form = ImportFileForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = ImportFileForm()
        obj = ImportFileModel.objects.get(activated=False)
        with open(obj.file.path, 'r', encoding='utf-8', errors='replace') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i == 0:
                    pass
                else:

                    row = "".join(row)
                    row = row.replace(";", "  ")
                    row = row.split("  ")
                    try:
                        date = datetime.datetime.strptime(row[0], '%m/%d/%Y')
                        new_item = date.strftime('%Y-%m-%d')
                    except ValueError:
                        new_item = row[0]
                    row[0] = new_item
                    RIDModel.objects.create(
                        Jour=row[0],
                        Prefecture=row[1],
                        csc=row[2],
                        TYPE=row[3],
                        ID=row[4],
                        STATUT_paquet=row[5],
                        Commentaire=row[6],
                    )
            obj.activated = True
            obj.save()
    return render(request, 'upload.html', {'form': form})


def home(request):
    return render(request, 'home.html')


def search(request):
    if request.method == "POST":
        searched = request.POST.get('searched')
        if searched is not None:
            RID = RIDModel.objects.filter(ID__contains=searched)
            return render(request, 'search.html', {'searched': searched, 'RID': RID})
    return render(request, 'search.html', {})
