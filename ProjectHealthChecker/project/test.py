__author__ = 'Thish'

import os

from project.csv_data import CsvData


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(BASE_DIR, "static/project/final.png")
path = '../static/project/final'
print path

c = CsvData
c.genreatesom()