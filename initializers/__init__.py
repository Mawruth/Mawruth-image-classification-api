import warnings
import os

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

warnings.filterwarnings('ignore')

from .app import app
from .model import model,class_names,data
import controllers