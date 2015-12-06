__author__ = 'Prabuddha'
import sys
import os

from numpy import genfromtxt

from project import sompy as SOM
from project.models import TrainingData
from numpy import array

class somtrain():

    def path(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        print BASE_DIR

    @staticmethod
    def genreatesom():

        """

        :rtype : object
        """
        # print paths
        print 'inside'
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        print 'Base: ' + BASE_DIR
        try:
            # Data = []
            # DataStr = ''
            # data = TrainingData.objects.all()
            # for obj in data:
            #     row = [float(obj.completed_project_duration), float(obj.spi), float(obj.cpi), float(obj.developer_experience), float(obj.test_cases_passed), float(obj.task_completion), float(obj.sprint_condition)]
            #     Data.append(row)
            # Data = array(Data)
            # pollution data
            Data = genfromtxt(open(os.path.join(BASE_DIR, "data_new.csv"), 'r'), dtype=float, delimiter=',')[1:]
            # Labels = Data[:, ]
            Data = Data[:, :11]
            # header = genfromtxt(open('whitewines.csv', 'r'), delimiter=',', dtype=None)[0]
            # header = header[0:]
            # header = header[np.newaxis, :]

            # print Labels
            print Data
            print Data.shape[0]
            print Data.shape[1]

            # with open('random data.csv') as csvfile:
            # reader = csv.DictReader(csvfile)
            # for row in reader:
            #    print(row['duration'])

            msz0 = 30
            msz1 = 30
            #
            dlen = Data.shape[0]
            sm = SOM.SOM('sm', Data, mapsize=[msz0, msz1], norm_method='var', initmethod='pca')
            sm.init_map()
            # setattr(sm, 'compname', header)
            # sm.view_map(what='codebook', which_dim='all', pack='Yes', text_size=7, save='Yes', save_dir='before_train')
            sm.train(n_job=1, shared_memory='no', verbose='off')
            # sm.view_map(what='codebook', which_dim='all', pack='Yes', text_size=2.8, save='Yes', save_dir='sompy')
            # sm.view_map(which_dim='all', pack='Yes', text_size=6, save='Yes', save_dir='after_train')
            #

            path = os.path.join(os.path.dirname(BASE_DIR), "media/project/final")
            filePath = os.path.join(os.path.dirname(BASE_DIR), "media/project/final.png")
            print path
            if os.path.isfile(filePath):
                os.remove(filePath)
            a = sm.view_U_matrix(dlen, distance2=1, row_normalized='No', show_data='Yes', contooor='Yes', blob='No', save='Yes',
                                 save_dir=path)

            # sm.hit_map()
            # sm.project_data(Data)
            # labels = sm.cluster(method='Kmeans', n_clusters=2)
            # sm.cluster_labels[:4]
            # cents = sm.hit_map_cluster_number()
        except:
            print "Unexpected Error:", sys.exc_info()
            return False
        else:
            while not os.path.isfile(filePath):
                if os.path.isfile(filePath):
                    return True

            return True

# c = somtrain()
# #c.path()
# c.genreatesom()


