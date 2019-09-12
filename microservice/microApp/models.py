from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=150)
    game = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Game(models.Model):
    name = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categorys')
    image = models.ImageField(upload_to='game')

    def __str__(self):
        return self.name.name 
