from django.shortcuts import render

# Create your views here.
def hello_formularz(request):
    if request.method == 'POST':
        name = request.POST['imie']
        return render(request, 'formularz_otrzymany.html', {'imie':name})
    else:
        return render(request, 'formularz.html')