# Springler Book Downloader

Projeto Python para realizar o Download em lote dos livros disponibilizados pela editora Springler em seu site durante o período de quarentena pela COVID-19

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install:

* Python 3.7 (https://www.python.org/downloads/release/python-370/)
* pip (https://pip.pypa.io/en/stable/installing/)
* virtualenv (https://virtualenv.pypa.io/en/latest/installation.html)

### Installing

A step by step series of examples that tell you how to get a development env running

Create a new Virtual Environment using Python 3.7. The example below creates a new python virtual env named `venv`

```
virtualenv -p python3.7 venv
```

Activate the new Virtual Environment

```
source venv/bin/activate
```

Install the dependencies used in the project

```
pip install -r requirements.txt
```

## Filtering the books you want


There is a file called `FreeEnglishTextBooks.xlsx` at the directory `xlsx` that holds all information about the books available. You should filter the book list in order to keep there only the books you want to download.
Note: The programa will download all the books that exists at the first sheet of the file.


## Running the program

To run the program, follow the steps below.

```
python3.7 main.py <path_to_source_file> <directory_to_save_downloaded_books>
```

* The first argument `path_to_source_file` specify the absolute path to the source file that holds the books information
* The second argument `directory_to_save_downloaded_books` specify the directory where you want to save the downloaded books. 

Note: If the directory does not exists, the program will create it.
Note2: The program will ovewrite the files if they already exists.


## Built With

* [Python 3.7](https://spring.io/projects/spring-boot) - The Java Web Framework User
* [xlrd] (https://pypi.org/project/xlrd/) - A MS Excel Integration library
* [Love]


## Contributing

Feel free to extend

## Authors

* **Marku Vinícius** - *Initial work* - [Marku Vinicius](https://github.com/markuvinicius)


## License

This project is licensed under the MIT License 

## Acknowledgments
