from django.shortcuts import render, get_object_or_404

from books.models import Category, Book


# Create your views here.
def Book_AllList(request, book_slug=None):
    category = None
    categories = Category.objects.all()
    books = Book.objects.filter(available=True)

    if book_slug:
        category = get_object_or_404(Category, slug=book_slug)
        books = Book.filter(category=category)

    return render(request,
                  'books/book/AllList.html',
                  {'category': category, 'categories': categories, 'books': books})


def Book_PublishedList(request):
    books = Book.available.all()
    return render(request,
                  'books/book/PublishedList.html',
                  {'books': books})


def book_AllDetail(request, id, slug):
    book = get_object_or_404(Book, id=id, slug=slug, available=True)
    return render(request,
                  'books/book/allDetail.html',
                  {'book': book})


def book_PublishedDetail(request, id):
    book = get_object_or_404(Book, id=id, status=Book.Status.AVAILABLE)
    return render(request, 'books/book/PublishedDetail.html')
