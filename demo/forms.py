from django import forms
from .models import (Book,
                     Author,
                     AuthorBook)
from django.forms import ModelForm

class BookForm(modelForm):

    class Meta:
        model = Book

class AuthorForm(modelForm):

    class Meta:
        model = Author

class AuthorBookForm(modelForm):

    class Meta:
        model = AuthorBook
