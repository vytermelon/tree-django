from django.contrib import admin
from .models import Book_id, Book_page

@admin.register(Book_id)
class Book_idAdmin(admin.ModelAdmin):
    list_display = ['username','book_id','bookname']

@admin.register(Book_page)
class Book_pageAdmin(admin.ModelAdmin):
    list_display = ['book_id','username', 'content', 'path','level','branch_name','node_id']
