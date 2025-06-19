from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.TextField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class Book(models.Model):

    STATUS_CHOICES = {
        'LENDO' : 'lendo',
        'CONCLUIDO': 'concluido',
        'PAUSADO':'pausado',
        'ABANDONADO':'abandonado'
    }


    title = models.TextField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=500, blank=True, default='')
    author = models.TextField(max_length=50, blank=True, default='')
    startDate = models.DateTimeField(default=timezone.now())
    finishDate = models.DateTimeField(blank=True),
    rating = models.IntegerField(default=1)
    status = models.TextField(max_length=10, choices=STATUS_CHOICES)
    owner = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    category = models.ManyToManyField(Category)


    def __str__(self):
        return f'{self.title} escrito por {self.author}. Leitura iniciado em: {self.startDate}'
    


