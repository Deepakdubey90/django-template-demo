from django.contrib import admin
from demo.models import (Book,
			 Author,
			 AuthorBook)

class AdminBlog(admin.ModelAdmin):
    pass

admin.site.register(Book, AdminBlog)
admin.site.register(Author, AdminBlog)
