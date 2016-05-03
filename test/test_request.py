import requests
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
#cosine_similarity(tfidf_matrix[0:1], tfidf_matrix)
response = requests.get('http://lookup.dbpedia.org/api/search/PrefixSearch?QueryClass=&MaxHits=5&QueryString=berl')
output  = re.compile('<description>(.*?)</description>', re.DOTALL |  re.IGNORECASE).findall(response.text)

tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(output)
a=cosine_similarity(tfidf_matrix[0:1], tfidf_matrix)

print tfidf_matrix.shape

