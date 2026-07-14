from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название книги")
    author = models.CharField(max_length=100, verbose_name="Автор книги")
    published_date = models.DateField(verbose_name="Дата публикации")
    genre = models.CharField(max_length=50, blank=True, verbose_name="Жанр")
    description = models.TextField(blank=True, verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return self.title


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews', verbose_name="Книга")
    reviewer_name = models.CharField(max_length=100, verbose_name="Имя рецензента")
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], 
        verbose_name="Оценка"
    )
    comment = models.TextField(blank=True, verbose_name="Комментарий")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"Рецензия от {self.reviewer_name} на {self.book.title}"