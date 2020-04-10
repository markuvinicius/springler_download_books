
class Book(object):
    __title = None
    __isbn = None
    __doi_code = None
    __download_url = "https://link.springer.com/content/pdf/{}%2F{}.pdf" 

    def __init__(self, title, doi_code , isbn):
        self.__title = str(title).replace('/','-').replace('.','-')
        self.__doi_code = doi_code
        self.__isbn = isbn

        self.__download_url = self.__download_url.format(doi_code,isbn)

    def get_download_url(self):
        return self.__download_url

    def get_title(self):
        return self.__title
