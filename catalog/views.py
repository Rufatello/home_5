from django.shortcuts import render
from catalog.models import Categoties, Product
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


def product(request, category_id):
    category = Categoties.objects.get(id=category_id)
    product_list = Product.objects.filter(categories_id=category)

    context = {
        'object_list': product_list,
        'category': category
    }
    return render(request, 'catalog/product.html', context)



def add_categories(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        descriptions = request.POST.get('descriptions')
        image = request.FILES.get('image')
        new_category = Categoties(name=name, descriptions=descriptions, image=image)
        new_category.save()
    return render(request, 'catalog/add_categories.html' )

