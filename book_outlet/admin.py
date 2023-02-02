from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    
    prepopulated_fields = {"slug": ("title",)}
    
    list_filter = ("author", "rating",)
    list_display = ("title", "author", "rating")
# Register your models here.
admin.site.register(Book, BookAdmin)