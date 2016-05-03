
import requests
import re
from decimal import *
import string

class Weight_factor():
    def __int__(self):
        self.skill_list=[]

    def print_file(self,skill_list):
        with open(self.skill_list) as sl:
            for skill in sl:
                print (skill)

    def cal_weight(self,skill_x_in_y_times,skill_y_in_x_times):
        return skill_x_in_y_times/skill_y_in_x_times, skill_y_in_x_times/skill_x_in_y_times

    def search_wiki_pedia(self,key_word,max_hit):
        key_word=key_word.replace(" ","_")
        # print key_word

        key='http://lookup.dbpedia.org/api/search/PrefixSearch?QueryClass=&MaxHits='+str(max_hit)+'&QueryString='+key_word
        response = requests.get(key)
        output  = re.compile('<description>(.*?)</description>', re.DOTALL |  re.IGNORECASE).findall(response.text)
        text=[]
        for doc in output:
            doc=doc.encode('ascii','ignore')
            text.append(doc.translate(string.maketrans("",""), string.punctuation))
        #First parameter is the replacement, second parameter is your input string
        return text

    def count_number(self,key,text):
        count=0
        key=key.lower()
        for i in range(0,len(text)):

            a=text[i].split()
            b=key.split()
            #len_doc=len_doc+len(a)
            for ii in a:
                ii=ii.lower()
                if ii==b[0]:
                    count=count+1
                    break
        return count


