from django.contrib import admin
from .models import *

#admin.site.register(Author),

#admin.site.register(Book),
admin.site.register(Genre),
admin.site.register(Language),
admin.site.register(Status),
 

#admin.site.register(BookInstance)
# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
admin.site.register(Author, AuthorAdmin)


class BookInstanceInline(admin.TabularInline):
    model = BookInstance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','price', 'genre', 'language', 'display_author')
    list_filter = ('genre','author')
    inlines = [BookInstanceInline]


@admin.register(BookInstance)
class BookInstance(admin.ModelAdmin):
    list_filter=('book', 'status')

