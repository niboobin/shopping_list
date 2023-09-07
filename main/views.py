from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'name': 'Obin',
        'class': 'PBP KKI'
    }

    return render(request, 'main.html', context)
