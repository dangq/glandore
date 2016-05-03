from src.weight_factor import Weight_factor
from decimal import *

# Open random no_sample skill_list
file_name='../src/s.txt'
list_skill=[]
with open(file_name,'r') as f:
    #f.readline()
    for line in f:

        line=line.replace('\n','')
        list_skill.append(line)
# Find number of keyword  in dbpedia
max_hit=10000
weight=Weight_factor()
weight_factor={}
for i in range(0,len(list_skill)):
    weight_factor[list_skill[i]]={}
    for j in range(0,len(list_skill)):
        print weight_factor

        if i==j:
            weight_factor[list_skill[i]][list_skill[j]]=1
        else:
            search_wiki_text=weight.search_wiki_pedia(list_skill[i],max_hit)
            no_key_word_1_text=weight.count_number(list_skill[i],search_wiki_text)
            no_key_word_2_text=weight.count_number(list_skill[j],search_wiki_text)
            #print list_skill[i]
            #print list_skill[j]
            if no_key_word_1_text==0:
                weight_factor[list_skill[i]][list_skill[j]]=0
            elif no_key_word_2_text==0:
                weight_factor[list_skill[i]][list_skill[j]]=0
            else:
                weight_factor[list_skill[i]][list_skill[j]]=Decimal(no_key_word_2_text)/Decimal(no_key_word_1_text)
print weight_factor

