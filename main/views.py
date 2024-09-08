from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306240162',
        'name': 'Farhan Adelio',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)