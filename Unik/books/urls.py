from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Регистрация и аутентификация
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='books/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='book_list'), name='logout'),

    # Книги
    path('', views.BookListView.as_view(), name='book_list'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('add_book/', views.BookCreateView.as_view(), name='add_book'),
    path('edit_book/<int:pk>/', views.BookUpdateView.as_view(), name='edit_book'),
    path('delete_book/<int:pk>/', views.BookDeleteView.as_view(), name='delete_book'),
    path('add_review/<int:book_id>/', views.add_review, name='add_review'),
]