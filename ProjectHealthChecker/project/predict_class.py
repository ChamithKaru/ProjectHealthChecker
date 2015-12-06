__author__ = 'Prabuddha'
import sklearn
from numpy import genfromtxt, savetxt
import os
from project.models import TrainingData
import numpy as np
import csv
import sys
import sompy as SOM
from matplotlib import pyplot as plt
from pandas import Series, DataFrame
from numpy import ndarray
from numpy import array


class predictor():
    def makePrediction(self):

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        #print Data
        Data = []
        DataStr = ''
        data = TrainingData.objects.all()
        for obj in data:
            row = [float(obj.completed_project_duration), float(obj.spi), float(obj.cpi), float(obj.developer_experience), float(obj.test_cases_passed), float(obj.task_completion), float(obj.sprint_condition)]
            Data.append(row)
        Data = array(Data)
        print Data
        # header = header[:0]
        # header = header[np.newaxis, :]
        # print Data
        def column(matrix, i):
             return [row[i] for row in matrix]
        X = Data[:, :6]
        Y = column(Data,6)
        from sklearn.naive_bayes import GaussianNB
        clf = GaussianNB()
        model=clf.fit(X, Y)
        #result=clf.predict([[80,0.905,0.9915,0.9,0.9844,0.99]])

        result=clf.predict([[40,0.8312,0.9118,0.4,0.8424,0.7800]])
        if result == 0:
             final_condition="Failed"
        else:
             final_condition="Success"
        print final_condition


p = predictor()
p.makePrediction()
