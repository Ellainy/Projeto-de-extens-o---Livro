from django.db import models

# Create your models here.
class Livro(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    idioma = models.CharField(max_length=50)
    capa = models.ImageField(upload_to='livros', null=True, blank=True)