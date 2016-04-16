import rdflib

graph = rdflib.Graph()
#graph.open("store", create=True)
#graph.parse("./SkillOntology.ttl",format='n3')

graph.parse("skills.owl")

#print out all the triples in the graph
#print len(graph)
a=0
for subject, predicate, object in graph:

     #a=a+len(subject)
     a=a+len(subject)

print a

# import re
# from collections import namedtuple
# from itertools import takewhile
#
# Entry = namedtuple('Entry', 'id name address phone')

# def get_entries(path):
#     with open(path) as file:
#         # an entry starts with `#@` line and ends with a blank line
#         for line in file:
#             if line.startswith('#@'):
#                 buf = [line]
#                 buf.extend(takewhile(str.strip, file)) # read until blank line
#                 yield Entry(*re.findall(r'<([^>]+)>', ''.join(buf)))
#
# print("\n".join(map(str, get_entries('SkillOntology.ttl'))))
