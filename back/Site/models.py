from django.db import models

class User(models.Model):
    nome    = models.CharField(max_length=50)
    senha   = models.CharField(max_length=50)


    def __str__(self):
        return self.nome
    
class Post(models.Model):
    titulo = models.CharField(max_length=30)
    desc = models.CharField(max_length=200)
    nome   = models.ForeignKey(
    User, on_delete=models.PROTECT
    )

    def __str__(self):
        return self.titulo
