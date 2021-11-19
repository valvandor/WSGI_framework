""" Module containing web application controllers — views """
from framework.templator import render


class Index:
    def __call__(self, request):
        return '200 OK', render('index.html')
