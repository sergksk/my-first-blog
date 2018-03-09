from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name="Автор")
    title = models.CharField("Заголовок", max_length=200)
    text = models.TextField("Содержание")
    created_date = models.DateTimeField("Дата создания", default=timezone.now)
    published_date = models.DateTimeField("Дата публикации", blank=True, null=True)
    count_comments = models.IntegerField(default=0)
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
   
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField("Автор", max_length=200)
    text = models.TextField("Комментарий")
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def approve(self):
         self.approved_comment = True
         self.save()
         self.post.count_comments += 1
         self.post.save()
         
    def approved_comments(self):
         return self.comments.filter(approved_comment=True)

    def __str__(self):
         return self.text