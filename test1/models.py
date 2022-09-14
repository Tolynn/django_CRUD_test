from django.db import models


class TestDB(models.Model):
    title = models.CharField(max_length=255)
    author=models.CharField(max_length=255, default=None)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT,
                            null=True)

    def __str__(self):
        return f'{self.title}'

class Category(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)

    def __str__(self):
        return f'{self.title}'
