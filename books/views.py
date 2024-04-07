from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from books.models import Book


class BookListView(generic.ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'
    paginate_by = 6


# class BookDetailView(generic.DetailView):
#     model = Book
#     template_name = 'books/book_detail.html'


def book_detail_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book_comments = book.comments.all()
    return render(request, 'books/book_detail.html', {'book': book, 'comments': book_comments})


class BookCreateView(generic.CreateView):
    model = Book
    fields = ('title', 'author', 'content', 'price', 'cover')
    template_name = 'books/book_creat.html'


class BookUpdateView(generic.UpdateView):
    model = Book
    fields = ('title', 'author', 'content', 'price', 'cover')
    template_name = 'books/book_update.html'


class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book_list')
