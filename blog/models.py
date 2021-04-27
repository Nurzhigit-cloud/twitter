from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,  verbose_name='User', blank=True, null=True)
    title = models.CharField(max_length=250)
    text = models.TextField(verbose_name='descrioptions')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'Статью'
        verbose_name_plural = 'Статьи'

    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title


#     @property
#     def number_of_comments(self):
#         return Comment.objects.filter(post_connected=self).count()
#
#
class Comment(models.Model):
    content = models.TextField(max_length=150)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_connected = models.ForeignKey(Post, on_delete=models.CASCADE)
