from django.db import models
from django.urls import reverse

class Author(models.Model):  
    full_name = models.TextField()  
    birth_year = models.SmallIntegerField()  
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name

class Publisher(models.Model):  
    title = models.TextField()  
    def __str__(self):
        return self.title

class Friend(models.Model):  
    f_name = models.TextField()  
    def __str__(self):
        return self.f_name


class Book(models.Model):  
    ISBN = models.CharField(max_length=13)  
    title = models.TextField()  
    description = models.TextField()  
    year_release = models.SmallIntegerField()  
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    price = models.DecimalField(default=None, max_digits=6, decimal_places=2)
    copy_count = models.SmallIntegerField(default=1)
    publisher = models.ForeignKey(Publisher, blank=True, null=True, on_delete=models.CASCADE)
    friend = models.ForeignKey(Friend, blank=True, null=True, on_delete=models.CASCADE)
    avatar = models.ImageField(verbose_name='Изображение книги', blank=True)
    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('author-detail', kwargs={'pk': self.pk}) 