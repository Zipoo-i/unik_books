from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.db.models import Q
from .models import Book, Review
from .forms import BookForm, ReviewForm, UserRegisterForm


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'
    paginate_by = 12

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(author__icontains=query)
            )
        return queryset


class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('book_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('book_list')

    def dispatch(self, request, *args, **kwargs):
        book = self.get_object()
        if not request.user.is_staff:
            return redirect('book_list')
        return super().dispatch(request, *args, **kwargs)


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'books/book_confirm_delete.html'
    success_url = reverse_lazy('book_list')

    def dispatch(self, request, *args, **kwargs):
        book = self.get_object()
        if not request.user.is_staff:
            return redirect('book_list')
        return super().dispatch(request, *args, **kwargs)


@login_required
def add_review(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.reviewer_name = request.user.username
            review.save()
            return redirect('book_detail', pk=book_id)
    else:
        form = ReviewForm()
    
    return render(request, 'books/add_review.html', {
        'form': form,
        'book': book
    })


class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'books/register.html'  # Убедитесь, что у вас есть этот шаблон
    success_url = reverse_lazy('login')