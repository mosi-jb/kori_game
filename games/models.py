from django.db import models


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=225, db_index=True)
    image = models.ImageField(upload_to='images/category')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'ژانر'
        verbose_name_plural = 'ژانر ها'


class Game(models.Model):
    title = models.CharField(max_length=225, db_index=True)
    image = models.ImageField(upload_to='images/game')
    category = models.ManyToManyField(Category, related_name='games')
    story = models.TextField()
    game_play = models.CharField(max_length=48, null=True, blank=True)
    slug = models.SlugField(unique=True, allow_unicode=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'بازی'
        verbose_name_plural = 'بازی ها'
