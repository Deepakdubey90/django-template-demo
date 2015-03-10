from django.shortcuts import render_to_response
from django.http import JsonResponse
from django.template import Context, loader
from django.http import HttpResponse
from uuid import uuid4
from .models import (Author,
                     Book,
                     AuthorBook)
from .forms import (AuthorForm,
                    AuthorBookForm,
                    BookForm)
from django import forms


def index(request):
    print("Index views get called!!!!!!!!!!")
    book_form = BookForm()
    author_form = AuthorForm()

    if request.method == 'GET':
        book_list = Book.objects.all()
        author_list = Author.objects.all()
        t = loader.get_template('book_collection.html')
        c = Context({'book_list': book_list, 'author_list': author_list, })
        return HttpResponse(t.render(c))
        #return render_to_response('author-book.html', locals())


def authorBookDetails(request):

    CATEGORY_CHOICES = {
        'M':'M',
        'F':'F'
    }

    MARITAL_STATUS = {
        'S':'S',
        'M':'M',
        'O':'O'
    }

    BOOK_CATEGORY = {
        'T':'T',
        'M':'M',
        'S':'S',
        'Mg':'M'
    }

    return render_to_response('author-book.html', locals())


def postAuthorBookDetails(request):
    """ save Author, Book details....... """

    print("This views get called!!!!!!!!!!")
    if request.method == 'POST':
        print("called inside post")
        book_form = BookForm(request.POST)
        author_form = AuthorForm(request.POST)
        print("\nbook_form data :::",book_form)
        print("\nauthor_form data :::",author_form)
        print("\nrequest value is ok", request.POST)
        print("Book Form data is", book_form)
        if book_form.is_valid():
            print("called inside if condition")
            book_form.save(commit=False)
            if author_form.is_valid():
                author_form.save()
                book_form.save()
                response = JsonResponse({"status":"success"})
                return HttpResponse(response)
            else:
                response = JsonResponse({"author validation error":author_form.errors})
                return HttpResponse(response)

        else:
            response = JsonResponse({"Book validation error":book_form.errors})
            return HttpResponse(response)
    else:
        return HttpResponse("Some error occured!!!!!!!!")
