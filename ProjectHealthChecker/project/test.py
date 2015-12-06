__author__ = 'Thish'

import os

from project.somtrain import somtrain
from project.models import TrainingData
from django.conf import settings
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ProjectHealthChecker.settings")

a = TrainingData.objects.all()
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# path = os.path.join(BASE_DIR, "static/project/final.png")
# path = '../static/project/final'
# print path
#
# c = somtrain
# c.genreatesom()

