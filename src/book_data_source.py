import xlrd
from book import Book

class BookDataSource(object):
    __path_to_books_source = None
    __work_book = None

    def __init__(self, path_to_source=None):
        self.__path_to_books_source = path_to_source
        self.__work_book = xlrd.open_workbook(self.__path_to_books_source)     

    def get_books(self):
        sheet = self.__work_book.sheet_by_index(0)
        book_list = []

        for line in range(1,sheet.nrows):
            row = sheet.row_values(line)                        
            book = Book(row[0], str(row[17]).split("/")[3] , row[7])
            book_list.append(book)            

        return book_list
        
        


        
        