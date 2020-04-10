from book_data_source import BookDataSource
from book_downloader import BookDownloader
import sys
from os import path
from os import mkdir

def check_source_file(book_source_xls=None):
    if not( ( path.exists(book_source_xls) ) & ( path.isfile(book_source_xls)) ):        
        raise RuntimeError("Data Source Invalid/Not Found")

    return True

def check_destination_dir(destination_dir=None):
    if not ( (path.exists(destination_dir) ) & (path.isdir(destination_dir) ) ):
        mkdir(destination_dir)

    return True

def book_repository(books_data_source=None):    
    books_source = BookDataSource(books_data_source)
    return books_source.get_books()


def book_download(books_list, destination_dir=None):    
    book_downloader = BookDownloader(destination_dir)
    for book in books_list:
        book_downloader.download_file(book)
        print('Livro {} salvo com sucesso'.format(book.get_title()))


if __name__ == '__main__':

    if len(sys.argv) < 3:
        raise RuntimeError("Usage: main.py <path_to_source_sheet> <destination_directory>")

    if not check_source_file(sys.argv[1]):
        exit(1)

    if not check_destination_dir(sys.argv[2]):
        exit(1)

    books = book_repository(sys.argv[1])
    book_download(books, sys.argv[2])