from django.shortcuts import render, get_object_or_404
from .models import Book
from django.db.models import Q

def home(request):
    search_query = request.GET.get('search', '')
    if search_query:
        books = Book.objects.filter(Q(title__icontains=search_query) | Q(author__icontains=search_query))
    else:
        books = Book.objects.all().order_by('-id')[:50]
    return render(request, 'books/home.html', {
        'books': books,
    })

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {
        'book': book,
    })

def about(request):
    return render(request, 'books/about.html')

def contact(request):
    return render(request, 'books/contact.html')

def donate(request):
    return render(request, 'books/donate.html')