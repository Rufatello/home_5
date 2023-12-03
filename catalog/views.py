from catalog.models import Categoties, Product, Blog
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View

from django.urls import reverse_lazy
from pytils.translit import slugify
from django.utils.text import slugify


class CategotiesListView(ListView):
    model = Categoties
    template_name = 'catalog/catalog.html'


class BlogListView(ListView):
    model = Blog

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(on_published=True)
        return queryset


class SlugifyBlogMixin:
    def form_valid(self, form):
        block = form.save(commit=False)
        block.slug = slugify(block.title)
        block.save()
        return super().form_valid(form)


class BlogCreateView(SlugifyBlogMixin, CreateView):
    model = Blog
    fields = ('title', 'body', 'photo')
    template_name = 'catalog/block_create.html'
    success_url = reverse_lazy('catalog:block_list')


class BlogUpdateView(SlugifyBlogMixin, UpdateView):
    model = Blog
    fields = ('title', 'body', 'photo')
    template_name = 'catalog/block_update.html'
    success_url = reverse_lazy('catalog:block_list')


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_view += 1
        self.object.save()
        return self.object


class HomeCreateView(CreateView):
    def get(self, request):
        return render(request, 'catalog/home.html')


class ContactView(View):
    template_name = 'catalog/contact.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        if request.method == 'POST':
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            print(name, phone, message)
        return render(request, self.template_name)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/views_product.html'


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        category = Categoties.objects.get(id=category_id)
        return Product.objects.filter(categories=category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs['category_id']
        context['category'] = Categoties.objects.get(id=category_id)
        return context


class AddCategoriesCreateView(CreateView):
    model = Categoties
    fields = ('name', 'descriptions', 'image')
    template_name = 'catalog/add_categories.html'
    success_url = reverse_lazy('catalog:catalog')
