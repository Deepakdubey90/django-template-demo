from django.db import models


class Book(models.Model):
    """  stores books details  """
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    publish_date = models.DateField(null=True)
    price = models.CharField(max_length=20)
    publication = models.CharField(max_length=32)


class Author(models.Model):
    """ store author details """

    CATEGORY_CHOICES = (
        ('M','Male'),
        ('F','Female'),
    )

    MARITAL_STATUS = (
        ('S','Single'),
        ('M','Married'),
        ('O','Other')
    )

    BOOK_CATEGORY =(
        ('T','Technical'),
        ('M','Management'),
        ('S','Story'),
        ('Mg','Magzine')
    )

    id = models.BigIntegerField(primary_key=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    gender = models.CharField(max_length=100, choices = CATEGORY_CHOICES)
    published_books = models.CharField(max_length=200,choices = BOOK_CATEGORY, null=True)
    dob =models.DateField(null=True)
    marital_status =models.CharField(max_length=100, choices = MARITAL_STATUS, null=True, blank=True)


class AuthorBook(models.Model):
    """ author and book details """

    id = models.BigIntegerField(primary_key=True)
    book = models.ForeignKey(Book)
    author = models.ForeignKey(Author)
