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

    gender = [
        {'id':'Male'},
        {'id':'Female'},
    ]

    MARITAL_STATUS = [
        {'ms':'Single'},
        {'ms':'Married'},
        {'ms':'Other'}
    ]

    BOOK_CATEGORY = [
        {'bc':'Technical'},
        {'bc':'Management'},
        {'bc':'Story'},
        {'bc':'Magzine'}
    ]
    return render_to_response('author-book.html', locals())



def postAuthorBookDetails(request):
    """ save Author, Book details....... """

    print("This views get called!!!!!!!!!!")
    if request.method == 'POST':
        print("called inside post")
        book_form = BookForm(request.POST)
        print("request value is ok", request.POST)
        print("Book Form data is", book_form)
        if book_form.is_valid():
            print("called inside if condition")
            book_form.save()
            response = JsonResponse({"status":"success"})
            return HttpResponse(response)
        else:
            response = JsonResponse({"validation error":book_form.errors})
            return HttpResponse(response)
    else:
        return HttpResponse("Some error occured!!!!!!!!")
