from django import forms
from .models import (Book,
                     Author,
                     AuthorBook)
from django.forms import ModelForm
from uuid import uuid4


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('name', 'publish_date', 'price', 'publication', )

class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author

class AuthorBookForm(forms.ModelForm):

    class Meta:
        model = AuthorBook
