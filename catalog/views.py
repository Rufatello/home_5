from catalog.models import Categoties, Product, Blog
from django.shortcuts import render
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from pytils.translit import slugify


class CategotiesListView(ListView):
    model = Categoties
    template_name = 'catalog/catalog.html'


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(on_published=True)
        return queryset


# class SlugifyBlogMixin:
#     def form_valid(self, form):
#         block = form.save(commit=False)
#         block.slug = slugify(block.title)
#         block.save()
#
#         return super().form_valid(form)


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'body', 'photo', 'on_published')
    template_name = 'catalog/block_create.html'
    success_url = reverse_lazy('catalog:block_list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()
        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'body', 'photo', 'on_published')
    template_name = 'catalog/block_update.html'
    success_url = reverse_lazy('catalog:block_list')


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_view += 1
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


class add_categoriesCreateView(CreateView):
    model = Categoties
    fields = ('name', 'descriptions', 'image')
    template_name = 'catalog/add_categories.html'
    success_url = reverse_lazy('catalog:catalog')


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'body', 'photo', 'on_published')
    template_name = 'catalog/block_create.html'
    success_url = reverse_lazy('catalog:block_list')
