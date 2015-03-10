from django.db import models
from django_extensions.db.fields import UUIDField


class Book(models.Model):
    """  stores books details  """

    id = UUIDField(primary_key=True)
    name = models.CharField(max_length=32)
    publish_date = models.DateField(null=True, blank=True)
    price = models.CharField(max_length=20)
    publication = models.CharField(max_length=32)


class Author(models.Model):
    """ store author details """

    CATEGORY_CHOICES = (
        ('M','M'),
        ('F','F'),
    )

    MARITAL_STATUS = (
        ('S','S'),
        ('M','M'),
        ('O','O'),
    )

    BOOK_CATEGORY = (
        ('T','T'),
        ('M','M'),
        ('S','S'),
        ('Mg','Mg'),
    )

    id = UUIDField(primary_key=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    gender = models.CharField(max_length=2, choices = CATEGORY_CHOICES, default='M')
    published_books = models.CharField(max_length=2, choices = BOOK_CATEGORY, null=True, default='T')
    dob =models.DateField(null=True)
    marital_status =models.CharField(max_length=2, choices = MARITAL_STATUS, null=True, blank=True, default='S')


class AuthorBook(models.Model):
    """ author and book details """

    id = UUIDField(primary_key=True)
    book = models.ForeignKey(Book)
    author = models.ForeignKey(Author)
