from django.db import models
from django.contrib.auth.models import User


translations_ru = {
    "title": "заголовок",
    "text": "основной текст",
    "image": "изображение",
    "date": "дата публикации",
    "time": "время публикации",
}

class Post(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name=translations_ru["title"]
    )
    text = models.TextField(
        max_length=1000,
        verbose_name=translations_ru["text"]
    )
    image = models.ImageField(
        verbose_name=translations_ru["image"],
        upload_to='blog/images/'
    )
    date = models.DateField(verbose_name=translations_ru["date"])
    time = models.TimeField(verbose_name=translations_ru["time"])
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='blog_posts')
    
    def __str__(self):
        return str(self.title)
