def get_args():
        parser = argparse.ArgumentParser(description='Parse the arguments!')
        # Add arguments
        parser.add_argument('filename')
        #parser.add_argument('-l', '--list', help='List of Skill')
        # Array for all arguments passed to script
        args = parser.parse_args()
        #print args
        #if len(args)==0 or len(args)>2:
         #   raise ValueError("Arguments are not allowed")
       # else:
            # Assign args to variables
        #name_skill_list = args.skill_list
            # Return all variable values
        return args.filename



def cal_weight(key1,key2):
    a=Weight_factor()
# key1='Java'
# key2='JVM'
    b= a.search_wiki_pedia(key1)
#print b
    count1,freq1=a.count_number(key2,b)
    count11,freq11=a.count_number(key1,b)
#print count1, count11
#print Decimal(count1)/Decimal(count11)


    b1= a.search_wiki_pedia(key2)
    count2,freq2=a.count_number(key1,b1)
    count22,freq22=a.count_number(key2,b1)
    return count1,count11,count2,count22




# key1_re_key2=1-log10(weight2/max(weight2,weight1))
# key2_re_key1=1-log10(weight1/max(weight1, weight2))

def extract_skill():

    columns = defaultdict(list) # each value in each column is appended to a list

    with open('yourskill.csv') as f:
        reader = csv.DictReader(f) # read rows into a dictionary format
        list_skill=[]
        for row in reader: # read a row as {column1: value1, column2: value2,...}
            for (k,v) in row.items(): # go over each column name and value
                if v:
                    if v not in list_skill:
                        list_skill.append(v)
    skill=sample(list_skill,100)
    with open('s.txt','wb') as f:
        for i in skill:
            f.writelines(i+'\n')


# def matrix_skill():


