import numpy as np
import pandas as pd
import ast
from nltk.stem.porter import PorterStemmer
import pickle



credits=pd.read_csv("D:/Movie Recommender/Raw_data/tmdb_5000_credits.csv")
movies=pd.read_csv("D:/Movie Recommender/Raw_data/tmdb_5000_movies.csv")
#print(movies.head())
#print(credits.head())
#merging two dataframes.
Final_movie=movies.merge(credits,on="title")
#print(Final_movie.shape)
# The columns we are going to keep for recomendations...
# id,genre,title,overview,keyword,cast,crew
Final_movie=Final_movie[['movie_id','title','overview','genres','keywords','cast','crew']]
#print(Final_movie.head())
#print(Final_movie.info())
#print(Final_movie.isnull().sum())
Final_movie.dropna(inplace=True)
#print(Final_movie.isnull().sum())
#print(Final_movie.duplicated().sum())
'''to make the genres column proper it is list of dictionaries.. and the whole is string'''
def convert(obj):
    L=[]
    for i in ast.literal_eval(obj):
        L.append(i['name'])
    return L
Final_movie['genres']=Final_movie['genres'].apply(convert)
#print(Final_movie['genres'])
Final_movie['keywords']=Final_movie['keywords'].apply(convert)
#print(Final_movie['keywords'])
def convert_cast(obj):
    L=[]
    counter=0
    for i in ast.literal_eval(obj):
        if counter !=3:
          L.append(i['name'])
          counter+=1
    return L
Final_movie['cast']=Final_movie['cast'].apply(convert_cast)
#print(Final_movie['cast'])
def convert_crew(obj):
    L=[]
    for i in ast.literal_eval(obj):
        if i['job'] =='Director':
          L.append(i['name'])
          break
    return L
Final_movie['crew']=Final_movie['crew'].apply(convert_crew)
#print(Final_movie['crew'])
Final_movie['overview']=Final_movie['overview'].apply(lambda x:x.split())
#print(Final_movie['overview'])
Final_movie['genres']=Final_movie['genres'].apply(lambda x:[i.replace(" ","") for i in x])
Final_movie['keywords']=Final_movie['keywords'].apply(lambda x:[i.replace(" ","") for i in x])
Final_movie['cast']=Final_movie['cast'].apply(lambda x:[i.replace(" ","") for i in x])
Final_movie['crew']=Final_movie['crew'].apply(lambda x:[i.replace(" ","") for i in x])
#print(Final_movie.head())
Final_movie['tags']=Final_movie['overview']+Final_movie['genres']+Final_movie['keywords']+Final_movie['cast']+Final_movie['crew']
new_movie_df=Final_movie[['movie_id','title','tags']]
new_movie_df['tags']=new_movie_df['tags'].apply(lambda x: " ".join(x))
new_movie_df['tags']=new_movie_df['tags'].apply(lambda x:x.lower())
#print(new_movie_df.head())
ps=PorterStemmer()
def stem(text):
    y=[]
    for i in text.split():
        y.append(ps.stem(i))
    return " ".join(y)
new_movie_df['tags']=new_movie_df['tags'].apply(stem)
pickle.dump(new_movie_df.to_dict(),open(r"../Raw_data/movies_dict.pkl","wb"))


