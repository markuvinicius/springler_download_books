import requests

class BookDownloader(object):

    def __init__(self, directory=None):
        self.__directory = directory

    def download_file(self, book=None):        
        document = requests.get(book.get_download_url())
        document_file = self.__directory + '/' + book.get_title() + '.pdf'
        open(document_file, 'wb').write(document.content)
