from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from test1.models import Category, TestDB


@admin.register(TestDB)
class TestDB(ModelAdmin):
    pass


@admin.register(Category)
class Category(ModelAdmin):
    pass
