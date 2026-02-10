from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
