from django.shortcuts import render
from catalog.models import Categoties
# Create your views here.
def catalog(request):
    Categoties_list = Categoties.objects.all()
    context = {
        'object_list': Categoties_list

    }
    return render(request, 'catalog/catalog.html', context)

def home(request):
    return render(request, 'catalog/home.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(name, phone, message)
    return render(request, 'catalog/contact.html')

