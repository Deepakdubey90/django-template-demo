from django import forms
from .models import (Book,
                     Author,
                     AuthorBook)
from django.forms import ModelForm

class BookForm(ModelForm):

    class Meta:
        model = Book
        exclude = []

class AuthorForm(ModelForm):

    class Meta:
        model = Author
        exclude = []

class AuthorBookForm(ModelForm):

    class Meta:
        model = AuthorBook
        exclude = []
