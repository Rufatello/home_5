from django.db import models

NO = {'blank': True, 'null':True}

class Categoties(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    descriptions = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='Categoties/', verbose_name='фото')

    def __str__(self):
        return f'{self.name}, {self.image}, {self.pk}'
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    descripsions = models.TextField(verbose_name='описание', **NO)
    image = models.ImageField(upload_to='products/', **NO, verbose_name='фото')
    categories = models.ForeignKey(Categoties, on_delete=models.CASCADE, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена')
    date_of_creation = models.DateField(verbose_name='дата создания', **NO)
    data_last = models.DateField(verbose_name='дата создания', **NO)

    def __str__(self):
        return f'{self.name}, {self.categories}, {self.price}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'



