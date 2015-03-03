from django.shortcuts import render_to_response
from django.template import Context, loader
from django.http import HttpResponse
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
    print("This views get called!!!!!!!!!!")
    if request.method == 'POST':
        print("called inside post")
        book_form = BookForm(instance=Book)
        author_form = AuthorForm(instance=Author)
        print("request value is ok ", request.POST)
        print("you enter in post request kookokoko")
        #if book_form.is_valid() or author_form.is_valid():
        print("called inside if condition")
        book_form.save()
        author_form.save()
        return HttpResponse("Success")
        #else:
        #return HttpResponse("Failure Occur..")
    else:
        #print("problems occurs!!!!!!!!!!!!!!!!!1111111")
        #return HttpResponse("Failure")
        return HttpResponse("Some error occured!!!!!!!!")




#def post(request):
