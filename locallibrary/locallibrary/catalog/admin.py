from django.contrib import admin

# Register your models here.
from .models import Author, Book, BookInstance, Genre, Language
# 在管理界面去改变一个模型的展示方式，当你定义了 ModelAdmin 类（描述布局）和将其注册到模型中
# admin.site.register(Author)
# define the admin class


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name',
                    'date_of_birth', 'date_of_death')


# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

# 使用@register 装饰器来注册模型（这和 admin.site.register() 语法作用一样)
# admin.site.register(Book)
# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

# admin.site.register(BookInstance)
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back', 'id')


admin.site.register(Genre)
admin.site.register(Language)
