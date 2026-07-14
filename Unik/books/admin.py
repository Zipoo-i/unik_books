from django.contrib import admin
from .models import Book, Review

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'genre', 'created_at')
    list_filter = ('genre', 'published_date')
    search_fields = ('title', 'author', 'description')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'reviewer_name', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')