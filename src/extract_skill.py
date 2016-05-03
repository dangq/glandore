import csv
from collections import defaultdict
from random import sample

class Extract_skill():
    def extract(self,file_open,file_save,no_sample):
        with open(file_open) as f:
            reader = csv.DictReader(f) # read rows into a dictionary format
            list_skill=[]
            for row in reader: # read a row as {column1: value1, column2: value2,...}
                for (k,v) in row.items(): # go over each column name and value
                    if v:
                        if v not in list_skill:
                            list_skill.append(v)
        # Get 100 sample skills
        skill=sample(list_skill,no_sample)
        # Write to the file s.txt
        with open(file_save,'wb') as f:
            for i in skill:
                f.writelines(i+'\n')




