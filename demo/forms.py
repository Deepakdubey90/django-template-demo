from django import forms
from demo.models import (Book,
                         Author,
                         AuthorBook)
from django.forms import ModelForm
from uuid import uuid4


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = '__all__'

class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = '__all__'

class AuthorBookForm(forms.ModelForm):

    class Meta:
        model = AuthorBook
        exclude = ['book', 'author']
