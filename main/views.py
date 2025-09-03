from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406349285',
        'name': 'Freya Zahra Anindyabhakti',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)
# Create your views here.
