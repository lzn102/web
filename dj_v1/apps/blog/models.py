from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name="文章标题")
    author = models.CharField(max_length=20, verbose_name="文章作者")
    content = models.TextField(verbose_name="文章内容")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = "文章"
        verbose_name_plural = verbose_name


