from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import ExampleForm
from django.http import HttpResponseForbidden

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    # logic to handle form and create book
    ...

@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    # logic to edit book
    ...

@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
# Create your views here.
def test_form_view(request):
    if request.method == "POST":
        print("Form submitted!", request.POST.get("username"))
    return render(request, "form_example.html")