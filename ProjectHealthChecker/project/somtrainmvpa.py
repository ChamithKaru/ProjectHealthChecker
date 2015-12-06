__author__ = 'Thish'

__author__ = 'Chamith'

import time   # to get the execute time
import MySQLdb
import numpy as np
import os
from project.models import TrainingData
from django.conf import settings
from mvpa2.suite import *
from matplotlib import pylab
from pylab import *
import PIL
import PIL.Image
import StringIO


class somtrainmvpa():

    def generatesom(self):

        start_time = time.time()

        # db = MySQLdb.connect(host="localhost", #  host, usually localhost
        #                      user="root", #  username
        #                       passwd="", #  password
        #                       db="python") # name of the data base

        # curOne = db.cursor()
        # curTwo = db.cursor()

        dataArrayOne = []
        dataArrayTwo = []
        data = TrainingData.objects.all()
        for obj in data:
            row1 = [obj.spi, obj.cpi, obj.developer_experience, obj.task_completion]
            row2 = [obj.developer_experience, obj.test_cases_passed, obj.task_completion, obj.sprint_condition]
            dataArrayOne.append(row1)
            dataArrayTwo.append(row2)

        # curOne.execute("SELECT SPI,CPI,DeveloperExperience,TaskCompletion  FROM dataset4")
        # # curOne.execute("SELECT SPI,CPI,Result  FROM dataset3")
        # curTwo.execute("SELECT DeveloperExperience,TastCaseCompletion,TaskCompletion,ProjectCondition  FROM dataset3")
        # dataArrayOne = []
        # dataArrayTwo = []
        #
        # for row in curOne.fetchall():
        #     dataArrayOne.append(row)
        #
        # # appending unsuccesful dataset
        # # dataArrayOne.append([0.716,0.732,0.4,0.8])
        #
        #
        # for row in curTwo.fetchall():
        #     dataArrayTwo.append(row)

        datasetOne = np.array(dataArrayOne)
        print(datasetOne)
        datasetTwo = np.array(dataArrayTwo)
        print(datasetTwo)

        #display values of the data inputs
        namesOne = []
        for y in range(len(datasetOne)):
            namesOne.append(y+1)

        namesTwo = []
        for z in range(len(datasetTwo)):
            namesTwo.append(z+1)

        print "sdfsdfs"

        # from mvpa2 import *



        somOne = SimpleSOMMapper((50, 50), 400, learning_rate=0.05)
        # somTwo = SimpleSOMMapper((50, 75), 400, learning_rate=0.05)

        # som.train(dataset)
        somOne.train(datasetOne)
        # somTwo.train(datasetTwo)

        pl.imshow(somOne.K, origin='higer')
        # pl.imshow(somTwo.K, origin='higer')

        # mapped = som(colors)
        mappedOne = somOne(datasetOne)
        # mappedTwo = somTwo(datasetTwo)

        pl.title('U-matirx')
        # SOM's kshape is (rows x columns), while matplotlib wants (X x Y)
        for i, m in enumerate(mappedOne):
            if (i < 160):
                pl.text(m[1], m[0], namesOne[i], ha='center', va='center',
                        bbox=dict(facecolor='white', alpha=0.5, lw=0))
            elif(i < 200):
                pl.text(m[1], m[0], namesOne[i], ha='center', va='center',
                        bbox=dict(facecolor='green', alpha=0.5, lw=0))
            else:
                pl.text(m[1], m[0], namesOne[i], ha='center', va= 'center',
                        bbox=dict(facecolor='blue', alpha=0.5, lw=0))
        # for i, m in enumerate(mappedTwo):
        #     pl.text(m[1], m[0], namesTwo[i], ha='center', va='center',
        #             bbox=dict(facecolor='white', alpha=0.5, lw=0))


        #to show the figure
        print (time.time()-start_time)
        pl.show()
        #pl.savefig()

if __name__ == '__main__':
    print "Starting Rango population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProjectHealthChecker.settings')
    settings.configure()
    from rango.models import Category, Page
    # s = somtrainmvpa()
    # s.generatesom()

