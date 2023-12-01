from catalog.models import Categoties, Product, Block
from django.shortcuts import render
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from pytils.translit import slugify
class CategotiesListView(ListView):
    model = Categoties
    template_name = 'catalog/catalog.html'

class BlockListView(ListView):
  model = Block
  
  def get_queryset(self, *args, **kwargs):
      queryset = super().get_queryset(*args, **kwargs)
      queryset=queryset.filter(on_published=True)
      return queryset

class BlockCreateView(CreateView):
    model = Block
    fields = ('title', 'body', 'photo', 'on_published')
    template_name = 'catalog/block_create.html'
    success_url = reverse_lazy('catalog:block_list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()
        return super().form_valid(form)
class BlockUpdateView(UpdateView):
    model = Block
    fields = ('title', 'body', 'photo', 'on_published')
    template_name = 'catalog/block_update.html'
    # success_url = reverse_lazy('catalog:block_detail')


class BlockDetailView(DetailView):
    model = Block

    def get_object(self, queryset=None):
        self.object=super().get_object(queryset)
        self.object.count_view +=1
        self.object.save()
        return self.object


def home(request):
    return render(request, 'catalog/home.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(name, phone, message)
    return render(request, 'catalog/contact.html')


# def product(request, category_id):
#     category = Categoties.objects.get(id=category_id)
#     product_list = Product.objects.filter(categories_id=category)
#
#     context = {
#         'object_list': product_list,
#         'category': category
#     }
#     return render(request, 'catalog/product.html', context)


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/views_product.html'

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


'''FBV для продуктов'''
# def views_product(request, pk):
# #     product_item = Product.objects.get(pk=pk)
# #
# #     context = {
# #         'product': product_item,
# #     }
# #     return render(request, 'catalog/views_product.html', context)

