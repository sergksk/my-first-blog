from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name="Автор")
    title = models.CharField("Заголовок", max_length=200)
    text = models.TextField("Содержание")
    created_date = models.DateTimeField("Дата создания",
            default=timezone.now)
    published_date = models.DateTimeField("Дата публикации", blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField("Автор", max_length=200)
    text = models.TextField("Комментарий")
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text