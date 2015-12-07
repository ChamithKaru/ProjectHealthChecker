__author__ = 'Thish'

__author__ = 'Chamith'

import time   # to get the execute time
import MySQLdb
import numpy as np
import os
from project.models import TrainingData, CurrentData
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
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        dataArrayOne = []
        dataArrayTwo = []
        try:
            data = TrainingData.objects.all()
            for obj in data:
                row1 = [float(obj.spi), float(obj.cpi), float(obj.developer_experience), float(obj.task_completion)]
                row2 = [float(obj.developer_experience), float(obj.test_cases_passed), float(obj.task_completion), float(obj.sprint_condition)]
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
            cur = CurrentData.objects.all().order_by('-id')[0]
            print cur.id
            dataArrayOne.append([float(cur.spi),float(cur.cpi),float(cur.developer_experience),float(cur.task_completion)])
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

            # namesTwo = []
            # for z in range(len(datasetTwo)):
            #     namesTwo.append(z+1)

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
            path = os.path.join(os.path.dirname(BASE_DIR), "media/project/final")
            filePath = os.path.join(os.path.dirname(BASE_DIR), "media/project/final.png")
            print filePath
            #pl.show()
            pl.savefig(filePath)
        except:
            print "Unexpected Error:", sys.exc_info()
            return False
        else:
            while not os.path.isfile(filePath):
                if os.path.isfile(filePath):
                    return True

            return True

# s = somtrainmvpa()
# print s.generatesom()