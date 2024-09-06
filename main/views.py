from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Farrel Reksa Prawira',
        'npm' : '2306275286',
        'kelas' : 'A',
        'aplikasi' : 'Record Store'
    }
    return render(request, "main.html", context)