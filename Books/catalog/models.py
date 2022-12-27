from django.db import models
from django.urls import reverse
from django.views import generic

# Create your models here.
 

class Genre(models.Model):

    name = models.CharField(max_length=200,
    help_text="Введите жанр",
    verbose_name="Жанр книги")
    
    def __str__(self):
        return self.name
    
class Language(models.Model):

    name = models.CharField(max_length=200,
    help_text="Введите язык книги",
    verbose_name="язык книги"
    )

    def __str__(self):
        return self.name

class Author(models.Model):

    first_name = models.CharField(
        max_length=100,
        help_text="Введите имя автора",
        verbose_name="Имя автора"
    )

    last_name = models.CharField(
        max_length=100,
        help_text="Введите фамилию автора",
        verbose_name="Фамилия автора"
    )

    date_of_birth = models.DateField(
        help_text="Введите дату рождения",
        verbose_name="дата рождения",
        null=True, blank=True
    )

    date_of_death = models.DateField(
        help_text="Введите дату смерти",
        verbose_name="дата смерти",
        null=True, blank=True
    )

    def __str__(self):
        return self.last_name

    class Meta:
        ordering = ['last_name']

class Book(models.Model):
    img = models.ImageField(
        upload_to='photos/', blank=True, null=True,
         
        
        verbose_name="фото книги",
        help_text="загрузите картинку книги"
    )

    price = models.IntegerField(null=True,
        verbose_name="стоимость книги",
        help_text="Введите стоимость книги"
    )


    title = models.CharField(
        max_length=200,
        verbose_name="название книги",
        help_text="Введите название книги"
    )

    genre = models.ForeignKey('Genre', on_delete=models.CASCADE,
    help_text="Выберите жанр",
    verbose_name="жанр книги"
    )

    language = models.ForeignKey('Language',
    on_delete=models.CASCADE,
    help_text="Выберите язык",
    verbose_name="язык книги")

    author = models.ManyToManyField('Author',
    help_text="Выберите автора книги",
    verbose_name="Автор кнпиги"
    )

    summary = models.TextField(
        help_text="Введите описание книги",
        verbose_name="описание книги"
    )

    isbn = models.CharField( max_length=13,
        help_text="Введите ISBN (13 символов)",
        verbose_name="ISBN книги"
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        pass
    
    def display_author(self):
        return ', '.join([author.last_name for author in self.author.all()])
    display_author.short_description = 'Авторы'

    ves = models.IntegerField(null=True,
        verbose_name="вес книги",
        help_text="Введите вес книги в граммах"
    )

    height = models.IntegerField(null=True,
        verbose_name="Высота книги",
        help_text="Введите высоту книги в см"
    )

    width = models.IntegerField(null=True,
        verbose_name="Ширина книги",
        help_text="Введите ширину книги в см"
    )

    pages = models.IntegerField(null=True,
        verbose_name="Количество страниц",
        help_text="Введите количество страниц книги"
    )

    binding = models.BooleanField(null=False,
        default = 0,
        verbose_name="Переплет",
        help_text="Твердый - 1. Мягкий - 0."
    )

class Status(models.Model):
    name = models.CharField(
        max_length=20,
        help_text="Введите статус экземпляра книги",
        verbose_name="Статус экземпляра книги"
    )

    def __str__(self):
        return self.name

class BookInstance(models.Model):
    book = models.ForeignKey('Book', on_delete = models.CASCADE, null=True)
    inv_nom = models.CharField(max_length=20, null=True,
        help_text="Введите инвентарный номер экземпляра",
        verbose_name="Инвентарный номер")
    imprint = models.CharField(max_length=200,
        help_text="Введите издательство и год выпуска",
        verbose_name="Издательство")
    status = models.ForeignKey('Status', on_delete=models.CASCADE, null=True,
        help_text="Изменить состояние экземпляра",
        verbose_name="Статус экземпляра")
    due_back = models.DateField(null=True, blank=True,
        help_text="Введите конец срока статуса",
        verbose_name="Дата окончания статуса")

    def __str__(self):
        return '%s %s %s' % (self.inv_nom, self.book, self.status)

