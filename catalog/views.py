from catalog.models import Categoties, Product, Blog, Versions
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View
from catalog.forms import ProductForm, VersionsForm
from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from pytils.translit import slugify
from django.utils.text import slugify
from django.contrib.auth.mixins import UserPassesTestMixin
class ProductCreationMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated

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

class VersionMixin:

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()
        VersionsFormset = inlineformset_factory(Product, Versions, form=VersionsForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionsFormset(self.request.POST)
        else:

            context_data['formset'] = VersionsFormset()
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
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

        for product in context['object_list']:
            active_version = product.versions_set.filter(is_active=True).first()

            if active_version:
                product.active_version_number = active_version.numb_versions
                product.active_version_name = active_version.name_versions
            else:
                product.active_version_number = None
                product.active_version_name = None

        category_id = self.kwargs['category_id']
        context['category'] = Categoties.objects.get(id=category_id)
        return context


class AddCategoriesCreateView(CreateView):
    model = Categoties
    fields = ('name', 'descriptions', 'image')
    template_name = 'catalog/add_categories.html'
    success_url = reverse_lazy('catalog:catalog')


class ProductCreateView(ProductCreationMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/ProductCreate.html'
    success_url = reverse_lazy('catalog:catalog')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()
        VersionsFormset = inlineformset_factory(Product, Versions, form=VersionsForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionsFormset(self.request.POST)
        else:

            context_data['formset'] = VersionsFormset()
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class ProductUpdate(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/productUpdate.html'
    success_url = reverse_lazy('catalog:catalog')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()
        VersionsFormset = inlineformset_factory(Product, Versions, form=VersionsForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionsFormset(self.request.POST, instance=self.object)
        else:

            context_data['formset'] = VersionsFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)
