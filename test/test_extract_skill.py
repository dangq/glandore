#from ..src import extract_skill
from src.extract_skill import Extract_skill
import os


current_dir=os.getcwd()
upper_dir=os.path.dirname(current_dir)
file_open=upper_dir+'/src/yourskill.csv'
file_save=upper_dir+'/src/s.txt'

a=Extract_skill()
a.extract(file_open,file_save,10)