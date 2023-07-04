import random

from django.shortcuts import render, redirect


# Create your views here.
def hello_formularz(request):
    if request.method == 'POST':
        name = request.POST['imie']
        return render(request, 'formularz_otrzymany.html', {'imie': name})
    else:
        return render(request, 'formularz.html')


lst = []


def kosci(request):
    if request.method == 'POST':
        ilosc = request.POST['ilosc']
        rodzaj = request.POST['rodzaj']
        ilosc = int(ilosc)
        rodzaj = int(rodzaj)
        lst = []
        for _ in range(ilosc):
            lst.append(random.randint(1, rodzaj))
        return render(request, 'kosci2.html', {'wyniki': lst, 'ilosc': ilosc, 'kosc': rodzaj})
    return render(request, 'formularz_kosci.html')


lst = [
    'sławek Bo',
    'Gosia pe',
    'Kasia De'
]


def list_danych(request):
    if request.method == 'POST':
        imie = request.POST.get('imie')
        nazwisko = request.POST.get('nazwisko')
        lst.append(f"{imie} {nazwisko}")
        return render(request, 'dane.html', {'dane': lst})
    else:
        return render(request, 'dane.html', {'dane': lst})


def get_person(request, id):
    if id >= len(lst):
        return render(request, '404.html')
    return render(request, 'osoba.html', {"osoba": lst[id]})


def del_person(request, id):
    lst.pop(id)
    return redirect('/dane/')
