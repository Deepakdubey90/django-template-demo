import os
import django


def book():
    b = add_book('30b1cf99-8ce8-4b73-b376-baf6776132b0', 'C++', '2012-07-10 14:58:00.000000', '897', 'O really')
    b = add_book('ac22730d-6779-4910-8ec5-11cd35e0c0df', 'C#', '2012-07-10 14:58:00.000000', '1297', 'NIRALI')
    b = add_book('b80310b5-52db-4e33-9eb1-af1eb7cf9231', 'Python', '2012-07-10 14:58:00.000000', '847', 'Techmax')
    b = add_book('da867d7e-578d-4d72-8e98-5d3160aeb38a', 'Django Quick Start', '2012-07-10 14:58:00.000000', '520', 'Pragati')


def add_book(id, name, publish_date, price, publication):
    b = Book.objects.get_or_create(id=id, name=name, publish_date=publish_date, price=price, publication=publication)[0]
    return b


# Start execution here!
if __name__ == '__main__':
    print("Starting population script...")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')
    django.setup()
    from demo.models import Book
    book()
