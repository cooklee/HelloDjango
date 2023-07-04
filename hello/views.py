import random

from django.shortcuts import render, redirect

from hello.models import Person, Book, genre_choises


# Create your views here.


def hello(request):
    return render(request, 'hello.html')


def name(request):
    return render(request, 'name.html')


def losowy_napis(request):
    napisy = [
        'Sławek Bo',
        'Gosia Pe',
        'Piotrek de'
    ]
    napis = napisy[random.randint(0, len(napisy) - 1)]
    return render(request, 'ln.html', {'n': napis})


def losuj(request):
    liczba = random.randint(1, 100)
    return render(request, 'ln.html', {'n': liczba})


def kosci(request):
    k1 = random.randint(1, 100)
    k2 = random.randint(1, 100)
    k3 = random.randint(1, 100)
    return render(request, 'kosci.html', {'k1': k1, 'k2': k2, 'k3': k3})


def lottek(request):
    lst = list(range(1, 49))
    random.shuffle(lst)
    wylosowane = lst[:6]
    wylosowane.sort()
    return render(request, 'lotek.html', {'liczby': wylosowane})


def ll2(request, a, b):
    liczba = random.randint(a, b)
    return render(request, 'ln.html', {'n': liczba})


def rzut(request, ilosc, kosc):
    lst = []
    for _ in range(ilosc):
        lst.append(random.randint(1, kosc))
    return render(request, 'kosci2.html', {'wyniki': lst, 'ilosc': ilosc, 'kosc': kosc})



def PersonView(request):
    persons = Person.objects.all()
    last_name = request.GET.get('last_name','')
    first_name = request.GET.get('first_name','')
    persons = persons.filter(last_name__icontains=last_name)
    persons = persons.filter(first_name__icontains=first_name)
    return render(request, 'persons.html', {'persons':persons})


def add_person_view(request):
    if request.method == 'GET':
        return render(request, 'form_add_person.html')
    imie = request.POST.get('first_name')
    nazwisko = request.POST.get('last_name')
    p = Person()
    p.first_name = imie
    p.last_name = nazwisko
    p.save()
    return redirect('/persons/')


def show_books(request):
    title = request.GET.get('title', '')
    year = request.GET.get('year')
    books = Book.objects.all()
    books = books.filter(title__icontains=title)
    if year:
        books = books.filter(year=year)
    return render(request, 'show_books.html', {'books':books})

def add_book(request):
    if request.method == 'GET':
        return render(request, 'add_book.html', {'genres': genre_choises})
    title = request.POST.get('title')
    year = request.POST.get('year')
    genre = request.POST.get('genre')
    Book.objects.create(title=title, year=year, genre=genre)
    return redirect('/show_books/')


