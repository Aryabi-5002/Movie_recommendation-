import preprocessing as pre
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from preprocessing import Final_movie


movies=pre.new_movie_df
cv=CountVectorizer(max_features=5000,stop_words='english')
vectors=cv.fit_transform(movies['tags']).toarray()
#print(vectors)
similarity=cosine_similarity(vectors)
def recommend(movie):
   movie_index=movies[movies['title']==movie].index[0]
   distances=similarity[movie_index]
   movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
   titles=[]
   tags=[]
   for i in movie_list:
      titles.append(movies.iloc[i[0]].title)
      tags.append(Final_movie.iloc[i[0]].tags)
   return titles,tags


#recommend("Transformers")
