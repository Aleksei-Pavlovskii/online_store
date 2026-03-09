from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержимое")
    image = models.ImageField(
        upload_to="blog/images/", null=True, blank=True, verbose_name="Изображение"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    is_published = models.BooleanField(default=True, verbose_name="Признак публикации")
    views_counter = models.PositiveIntegerField(
        default=0, verbose_name="Счетчик просмотров"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "заголовок"
        verbose_name_plural = "заголовки"
        ordering = ["created_at"]
