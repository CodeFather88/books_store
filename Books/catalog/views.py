from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Book, Author, BookInstance, Genre
# Create your views here.
from django.views import generic
def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact=3).count()
    num_authors = Author.objects.count()
    books = Book.objects.all()
    return render(request, 'index.html',
        context={
             
            'books':books,
            'num_books':num_books,
            'num_instances':num_instances,
            'num_instances_available':num_instances_available,
            'num_authors':num_authors,
             
        }
    )


 
     
class BookDetailView(generic.DetailView):
    model = Book
    template_name='element.html'
     

class BookListView(generic.ListView):
    model = Book
    paginate_by = 3
    template_name=['element.html','index.html']

class BookListView1(generic.ListView):
    model = Book
     
    template_name= 'element.html' 

 
    

