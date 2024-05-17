from django.db import models

# Create your models here.
class Cate(models.Model):
    name=models.TextField(max_length=200, default='')

    def __str__(self):
        return self.name



class Article(models.Model):
    title=models.TextField(max_length=400, default='')
    des=models.TextField(max_length=3000, default='')
    date=models.DateField(default='')
    image=models.TextField()
    category=models.ForeignKey( Cate,  on_delete=models.CASCADE)
    
