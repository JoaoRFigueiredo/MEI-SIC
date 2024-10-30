from fastapi import APIRouter
from sqlmodel import select
from fastapi.responses import JSONResponse
from models import *
import pandas as pd
import os
import json
from sqlalchemy import create_engine
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
from fuzzywuzzy import process
import numpy as np
from sqlalchemy import desc
from scipy.sparse import csr_matrix
from sklearn.feature_extraction.text import CountVectorizer
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, HTTPException
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.neighbors import NearestNeighbors
from models import *
from database import *
from scipy.sparse import csr_matrix
load_dotenv()

router = APIRouter(prefix='/recommendation', tags=['Recomendation'])
engine = create_engine(os.getenv('DATABASE_URL_FILE'))

@router.get("/nonpersonalized", summary="Get non-personalized recommendations")
async def nonPersonalised():
    script_dir = os.path.dirname(__file__)
    path = os.path.join(script_dir, '../utils/NonPersonalized.json')
    if os.stat(path).st_size == 0:
        df = pd.read_sql_query("""SELECT 
            m.movieid,
            m.title,
            m.genres,
            m.imdbid,
            m.year,
            m.url,
            m.titlelower,
            COUNT(r.stars) AS count,
            AVG(r.stars) AS mean
            FROM 
                movie m
            JOIN 
                rating r ON m.movieid = r.movie_id
            GROUP BY 
                m.movieid, m.title, m.genres, m.imdbid, m.year, m.url, m.titlelower""", con=engine)
        m = 1000
        df['weighted_rating'] = ((df['count'] / (df['count'] + m)) * df['mean'] +(m / (df['count'] + m)) * df['mean'].mean())


        sorted_df = df.sort_values(by='weighted_rating', ascending=False)
        json_result = sorted_df.head(5).reset_index().to_dict(orient='records')
        with open(path, "w") as file:
            json.dump(json_result, file)
    
        return JSONResponse(content=json_result)
    else:
        with open(path, "r") as file:
            #return JSONResponse(content=file.read())
            data = json.load(file)
            return data
        
@router.get("/nonpersonalizedGenre/{genre}", summary="Get non-personalized recommendations with genre")
async def nonPersonalisedGenre(genre: str):
    script_dir = os.path.dirname(__file__)
    df = pd.read_csv(os.path.join(script_dir, "../utils/small_dataset/movies_rating.csv"))
    df['genres'] = df['genres'].str.split('|')
    best_movies_for_genres = {}
    genre_df = df[df['genres'].apply(lambda x: genre in x)]
    if not genre_df.empty:
        best_movie = genre_df[['movieId', 'title', 'url', 'count' ,'weighted_rating']].head(5)
        best_movies_for_genres = best_movie.to_dict(orient='records')
    return best_movies_for_genres

@router.get("/nonpersonalizedYear/{year}", summary="Get non-personalized recommendations with year")
async def nonPersonalisedYear(year: int):
    script_dir = os.path.dirname(__file__)
    df = pd.read_csv(os.path.join(script_dir, "../utils/small_dataset/movies_rating.csv"))
    df = df[df['year'] == year]
    movies_year_best = df[['movieId', 'title', 'url', 'count' ,'weighted_rating']].head(5)
    return movies_year_best.to_dict(orient='records')

@router.get("/nonpersonalizedDecade/{decade}", summary="Get non-personalized recommendations with decade")
async def nonPersonalisedDecate(decade: int):
    script_dir = os.path.dirname(__file__)
    df = pd.read_csv(os.path.join(script_dir, "../utils/small_dataset/movies_rating.csv"))
    df = df[df['decade'] == decade]
    movies_decade_best = df[['movieId', 'title', 'url', 'count' ,'weighted_rating']].head(5)
    return movies_decade_best.to_dict(orient='records')

@router.get("/nonpersonalizedOverall", summary="Get non-personalized recommendations overall")
async def nonPersonalisedOverall():
    script_dir = os.path.dirname(__file__)
    df = pd.read_csv(os.path.join(script_dir, "../utils/small_dataset/movies_rating.csv"))
    movies_overall_best = df[['movieId', 'title', 'url', 'count' ,'weighted_rating']].head(5)
    return movies_overall_best.to_dict(orient='records')

@router.get("/personalizedColaborative/{user_id}", summary="Get personalized recommendations by colaborative filtering")
async def personalisedColaborative(*, session: AsyncSession = Depends(get_db),user_id: int):
    query = select(Rating).where(Rating.user_id == user_id)
    result = await session.execute(query)
    rating = result.scalars().first()
    if not rating:
        raise HTTPException(status_code=404, detail="Ratings not found")
    script_dir = os.path.dirname(__file__)
    ratings = pd.read_csv(os.path.join(script_dir, "../recommender/dataset/small_dataset/ratings.csv"))
    movies = pd.read_csv(os.path.join(script_dir, "../recommender/dataset/small_dataset/movies_full_2.csv"))
    tags = pd.read_csv(os.path.join(script_dir, "../recommender/dataset/small_dataset/tags.csv"))
    

    # M = df['userId'].nunique()
    # N = df['movieId'].nunique()

    # user_mapper = dict(zip(np.unique(df["userId"]), list(range(M))))
    # movie_mapper = dict(zip(np.unique(df["movieId"]), list(range(N))))
    
    # user_inv_mapper = dict(zip(list(range(M)), np.unique(df["userId"])))
    # movie_inv_mapper = dict(zip(list(range(N)), np.unique(df["movieId"])))
    
    # user_index = [user_mapper[i] for i in df['userId']]
    # item_index = [movie_mapper[i] for i in df['movieId']]

    # X = csr_matrix((df["rating"], (user_index,item_index)), shape=(M,N))
    # ser_index = user_mapper[user_id]
    # similarities = cosine_similarity(X[user_index], X)

    # similar_users_indices = similarities.argsort()[0][-5-1:-1][::-1]

    # recommended_movies = {}

    # for similar_user_index in similar_users_indices:
    #     unrated_movies = np.where(np.logical_and(X[user_index].toarray()[0] == 0, X[similar_user_index].toarray()[0] != 0))[0]
        
    #     for movie_index in unrated_movies:
    #         if movie_index not in recommended_movies:
    #             recommended_movies[movie_index] = similarities[0, similar_user_index] * X[similar_user_index, movie_index]
    #         else:
    #             recommended_movies[movie_index] += similarities[0, similar_user_index] * X[similar_user_index, movie_index]

    # recommended_movies = sorted(recommended_movies.items(), key=lambda x: x[1], reverse=True)

    # recommended_movie_ids = [movie_inv_mapper[movie_index] for movie_index, _ in recommended_movies]

    # recommendations = recommended_movie_ids[:5]

    # movie_details = []
    # for movie_id in recommendations:
    #     movie_info = df_movies.loc[movie_id, ['title', 'url', 'genres', 'imdbId', 'year']]
    #     movie_details.append({
    #         'title': movie_info['title'],
    #         'url': movie_info['url'],
    #         'genres': movie_info['genres'],
    #         'imdbId': movie_info['imdbId'],
    #         'year': movie_info['year']
    #     })
    # return movie_details


    def create_weighted_rating_tags_df(movies_df, ratings_df, tags_df):
        movies_rating_user_df = pd.merge(movies_df, ratings_df, on="movieId", how="inner")

        movies_rating_df = movies_rating_user_df[['movieId', 'title', 'rating', 'genres', 'year', 'url']].groupby(['movieId', 'title', 'genres', 'year', 'url'])['rating'].agg(['count', 'mean']).round(1)
        movies_rating_df.sort_values('count', ascending=False, inplace=True)
        movies_rating_df.rename(columns={'count' : 'Num_ratings', 'mean': 'Average_rating'}, inplace=True)

        C = round(ratings_df['rating'].mean(), 2)
        m = 500
        movies_rating_df['Bayesian_rating'] = (movies_rating_df['Num_ratings'] / (movies_rating_df['Num_ratings'] + m)) * movies_rating_df['Average_rating'] + (m / (movies_rating_df['Num_ratings'] + m)) * C
        movies_rating_df.drop(columns='Average_rating', inplace=True)
        movies_rating_df.rename(columns={'Num_ratings' : 'count', 'Bayesian_rating' : 'weighted_rating'}, inplace=True)
        movies_rating_df.reset_index(inplace=True)
        

        movies_rating_tags_df = pd.merge(movies_rating_df, tags_df, how='left', on='movieId')
        movies_rating_tags_df['tag'] = movies_rating_tags_df['tag'].fillna(value='')
        movies_rating_tags_df = movies_rating_tags_df.groupby(['movieId', 'title', 'genres', 'year', 'url', 'count', 'weighted_rating'])['tag'].apply(list).reset_index()
        movies_rating_tags_df['genres'] = movies_rating_tags_df['genres'].str.split('|')
        movies_rating_tags_df['tag'] = movies_rating_tags_df['tag'].apply(lambda x: [] if x == [float('nan')] else x)
        movies_rating_tags_df.sort_values(by='weighted_rating', ascending=False, inplace=True)
        return movies_rating_tags_df
    
    # def create_utility_matrix(df):
    #     utility_matrix = df.pivot(index='userId', columns='movieId', values='rating').fillna(0)
    #     return utility_matrix



    # def collaborative_filtering_recommendation(df, user_id, k, num_recommendations):
    #     utility_matrix = create_utility_matrix(df)
    #     user_indices = {user_id: idx for idx, user_id in enumerate(utility_matrix.index)}
    #     if user_id not in user_indices:
    #         print("User ID does not exist.")
    #         return []
    #     user_similarity = cosine_similarity(utility_matrix)
    #     knn = NearestNeighbors(n_neighbors=k, metric='cosine')
    #     knn.fit(user_similarity)
    #     _, indices = knn.kneighbors([user_similarity[user_indices[user_id]]])
    #     neighbor_ratings = utility_matrix.iloc[indices[0]]
    #     item_ratings = neighbor_ratings.mean(axis=0)
    #     user_ratings = utility_matrix.loc[user_id]
    #     recommended_items = item_ratings[user_ratings == 0].sort_values(ascending=False).index.tolist()[:num_recommendations]
        
    #     # # Filter out recommended items based on user preferences
    #     # if user_preferences['disliked_genres']:
    #     #     df_filtered = movies_rating_tags_df[~movies_rating_tags_df['genres'].apply(lambda x: any(genre in user_preferences['disliked_genres'] for genre in x))]
    #     #     recommended_items = [item for item in recommended_items if item in df_filtered['movieId']]
        
    #     return movies_rating_tags_df.loc[recommended_items, 'movieId'].tolist()
    
    movies_rating_tags_df = create_weighted_rating_tags_df(movies, ratings, tags)

    # movies_recomend_ids = collaborative_filtering_recommendation(ratings, user_id, 5, 5)

    def create_X(df):
    
        M = df['userId'].nunique()
        N = df['movieId'].nunique()

        user_mapper = dict(zip(np.unique(df["userId"]), list(range(M))))
        movie_mapper = dict(zip(np.unique(df["movieId"]), list(range(N))))
        
        user_inv_mapper = dict(zip(list(range(M)), np.unique(df["userId"])))
        movie_inv_mapper = dict(zip(list(range(N)), np.unique(df["movieId"])))
        
        user_index = [user_mapper[i] for i in df['userId']]
        item_index = [movie_mapper[i] for i in df['movieId']]

        X = csr_matrix((df["rating"], (user_index,item_index)), shape=(M,N))
        
        return X, user_mapper, movie_mapper, user_inv_mapper, movie_inv_mapper

    


    def collaborative_filtering_recommendation(movie_id, X, movie_mapper, movie_inv_mapper, k, metric='cosine'):
        X = X.T
        neighbour_ids = []
        
        movie_ind = movie_mapper[movie_id]
        movie_vec = X[movie_ind]
        if isinstance(movie_vec, (np.ndarray)):
            movie_vec = movie_vec.reshape(1,-1)
        # use k+1 since kNN output includes the movieId of interest
        kNN = NearestNeighbors(n_neighbors=k+1, algorithm="brute", metric=metric)
        kNN.fit(X)
        neighbour = kNN.kneighbors(movie_vec, return_distance=False)
        for i in range(0,k):
            n = neighbour.item(i)
            neighbour_ids.append(movie_inv_mapper[n])
        neighbour_ids.pop(0)
        return neighbour_ids
    

    X, user_mapper, movie_mapper, user_inv_mapper, movie_inv_mapper = create_X(ratings)

    collaborative_filtering_recommendations_ids = collaborative_filtering_recommendation(1, X, movie_mapper, movie_inv_mapper, k=10)


    movies_recomend_df = movies_rating_tags_df[movies_rating_tags_df['movieId'].isin(collaborative_filtering_recommendations_ids)]
    
    return movies_recomend_df.to_dict(orient='records')



@router.get("/personalizedContent", summary="Get personalized recommendations by content filtering")
async def personalisedContent(*, session: AsyncSession = Depends(get_db), title: str, user_id: int):
    script_dir = os.path.dirname(__file__)
    movies_df = pd.read_csv(os.path.join(script_dir,"../recommender/dataset/small_dataset/movies_full_2.csv"))
    ratings_df = pd.read_csv(os.path.join(script_dir,"../recommender/dataset/small_dataset/ratings.csv"))
    tags_df = pd.read_csv(os.path.join(script_dir,"../recommender/dataset/small_dataset/tags.csv"))
    
    def create_weighted_rating_tags_df(movies_df, ratings_df, tags_df):
        movies_rating_user_df = pd.merge(movies_df, ratings_df, on="movieId", how="inner")

        movies_rating_df = movies_rating_user_df[['movieId', 'title', 'rating', 'genres', 'year', 'url']].groupby(['movieId', 'title', 'genres', 'year', 'url'])['rating'].agg(['count', 'mean']).round(1)
        movies_rating_df.sort_values('count', ascending=False, inplace=True)
        movies_rating_df.rename(columns={'count' : 'Num_ratings', 'mean': 'Average_rating'}, inplace=True)

        C = round(ratings_df['rating'].mean(), 2)
        m = 500
        movies_rating_df['Bayesian_rating'] = (movies_rating_df['Num_ratings'] / (movies_rating_df['Num_ratings'] + m)) * movies_rating_df['Average_rating'] + (m / (movies_rating_df['Num_ratings'] + m)) * C
        movies_rating_df.drop(columns='Average_rating', inplace=True)
        movies_rating_df.rename(columns={'Num_ratings' : 'count', 'Bayesian_rating' : 'weighted_rating'}, inplace=True)
        movies_rating_df.reset_index(inplace=True)
        

        movies_rating_tags_df = pd.merge(movies_rating_df, tags_df, how='left', on='movieId')
        movies_rating_tags_df['tag'] = movies_rating_tags_df['tag'].fillna(value='')
        movies_rating_tags_df = movies_rating_tags_df.groupby(['movieId', 'title', 'genres', 'year', 'url', 'count', 'weighted_rating'])['tag'].apply(list).reset_index()
        movies_rating_tags_df['genres'] = movies_rating_tags_df['genres'].str.split('|')
        movies_rating_tags_df['tag'] = movies_rating_tags_df['tag'].apply(lambda x: [] if x == [float('nan')] else x)
        movies_rating_tags_df.sort_values(by='weighted_rating', ascending=False, inplace=True)
        return movies_rating_tags_df
    
    def find_movie_indices(df, title):
        df_copy = df.copy()
        df_copy['features'] = df_copy['genres'] + df_copy['tag'] + df_copy['title'].apply(lambda x: [x])  # Add movie titles to features
        
        df_copy['features'] = df_copy['features'].apply(lambda x: ' '.join(x))  # Ensure 'features' is a string
        
        # TF-IDF Vectorization
        tfidf_vectorizer = TfidfVectorizer(stop_words='english')
        tfidf_matrix = tfidf_vectorizer.fit_transform(df_copy['features'])
        
        # Calculate cosine similarity
        cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
        idx = df_copy.index[df_copy['title'] == title].tolist()[0]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        movie_indices = [i[0] for i in sim_scores]
        movie_indices = movie_indices[1:30]
        del df_copy
        return movie_indices

    def recommend_movies(df, movie_indices, preferred_genres=None, disliked_genres=None):
        recommended_movies = []
        neutral_movies = []

        for i in movie_indices:
            movie_genres = set(df.loc[i, 'genres'])
            print(movie_genres)

            # Skip movies with disliked genres
            if disliked_genres and movie_genres.intersection(set(disliked_genres)):
                continue

            # Collect movies with preferred genres
            if preferred_genres and movie_genres.intersection(set(preferred_genres)):
                recommended_movies.append(i)
            
            # Collect neutral movies (no preferred or disliked genres)
            elif preferred_genres and not movie_genres.intersection(set(preferred_genres)) and not movie_genres.intersection(set(disliked_genres)):
                neutral_movies.append(i)
            
            # Limit the number of recommended movies to 5
            if len(recommended_movies) >= 5:
                break

        # If there are less than 5 recommended movies with preferred genres, add neutral movies
        if len(recommended_movies) < 5:
            for neutral_movie in neutral_movies:
                recommended_movies.append(neutral_movie)
                if len(recommended_movies) >= 5:
                    break

 

        recommended_movies_df = df.loc[recommended_movies]
        recommended_movies_df = recommended_movies_df[['title', 'year', 'url', 'count', 'weighted_rating', 'genres']]
        return recommended_movies_df
    
    df = create_weighted_rating_tags_df(movies_df, ratings_df, tags_df)

    user = await session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    preferred_genres = user.genresLike
    disliked_genres = user.genresDislike
 
    movie_indices_list = find_movie_indices(df, title)
    recommended_movies = recommend_movies(df, movie_indices_list, preferred_genres, disliked_genres).to_dict(orient='records')
    
    return recommended_movies
    
@router.get("/personalizedKnowledge/{user_id}", summary="Get personalized recommendations by knowledge filtering")
async def personalisedknowledge(*, session: AsyncSession = Depends(get_db), user_id: int):
    script_dir = os.path.dirname(__file__)
    movies_df = pd.read_csv(os.path.join(script_dir,"../recommender/dataset/small_dataset/movies_full_2.csv"))
    ratings_df = pd.read_csv(os.path.join(script_dir,"../recommender/dataset/small_dataset/ratings.csv"))
    
    def create_weighted_rating_df(movies_df, ratings_df):
        movies_rating_user_df = pd.merge(movies_df, ratings_df, on="movieId", how="inner")

        movies_rating_df = movies_rating_user_df[['movieId', 'title', 'rating', 'genres', 'year', 'url']].groupby(['movieId', 'title', 'genres', 'year', 'url'])['rating'].agg(['count', 'mean']).round(1)
        movies_rating_df.sort_values('count', ascending=False, inplace=True)
        movies_rating_df.rename(columns={'count' : 'Num_ratings', 'mean': 'Average_rating'}, inplace=True)

        C = round(ratings_df['rating'].mean(), 2)
        m = 500
        movies_rating_df['Bayesian_rating'] = (movies_rating_df['Num_ratings'] / (movies_rating_df['Num_ratings'] + m)) * movies_rating_df['Average_rating'] + (m / (movies_rating_df['Num_ratings'] + m)) * C
        movies_rating_df.drop(columns='Average_rating', inplace=True)
        movies_rating_df.sort_values(by='Bayesian_rating', ascending=False, inplace=True)
        movies_rating_df.rename(columns={'Num_ratings' : 'count', 'Bayesian_rating' : 'weighted_rating'}, inplace=True)
        movies_rating_df.reset_index(inplace=True)
        movies_rating_df['genres'] = movies_rating_df['genres'].str.split('|')
        return movies_rating_df
    
    def recommend_movies_based_on_genres(df, preferred_genres=None, disliked_genres=None):
        df_copy = df.copy()
        recommended_movies_ids = []
        
        for idx, row in df_copy.iterrows():
            movie_genres = set(row['genres'])
            
            # Check if the movie does not have any of the disliked genres
            if disliked_genres:
                if movie_genres.intersection(set(disliked_genres)):
                    continue

            # Check if the movie has any of the preferred genres
            if preferred_genres:
                if not movie_genres.intersection(set(preferred_genres)):
                    continue
            
            # Add the movie to the list of recommendations
            recommended_movies_ids.append(idx)
            
            # Limit the number of recommended movies to 10
            if len(recommended_movies_ids) >= 5:
                break

        recommended_movies_df = df.loc[recommended_movies_ids]
        recommended_movies_df = recommended_movies_df[['title', 'year', 'url', 'count', 'weighted_rating', 'genres']]

        return recommended_movies_df

    user = await session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    preferred_genres = user.genresLike
    disliked_genres = user.genresDislike
    df = create_weighted_rating_df(movies_df, ratings_df)

    recommended_movies_df = recommend_movies_based_on_genres(df, preferred_genres, disliked_genres)
    return recommended_movies_df.to_dict(orient='records')




@router.get("/personalizedHybrid", summary="Get personalized recommendations by hybrid filtering")
async def personalisedHybrid(*, session: AsyncSession = Depends(get_db), user_id: int):
    user_id = user_id
    script_dir = os.path.dirname(__file__)
    movies = pd.read_csv(os.path.join(script_dir,"../recommender/dataset/small_dataset/movies_full_2.csv"))
    ratings = pd.read_csv(os.path.join(script_dir,"../recommender/dataset/small_dataset/ratings.csv"))
    tags = pd.read_csv(os.path.join(script_dir,"../recommender/dataset/small_dataset/tags.csv"))

    rated_movie_ids = ratings[ratings['userId'] == user_id]['movieId'].unique()


    def create_weighted_rating_tags_df(movies_df, ratings_df, tags_df): # vamos retirar deste dataframe os filmes que o user já deu rating
        movies_rating_user_df = pd.merge(movies_df, ratings_df, on="movieId", how="inner")

        movies_rating_df = movies_rating_user_df[['movieId', 'title', 'rating', 'genres', 'year', 'url']].groupby(['movieId', 'title', 'genres', 'year', 'url'])['rating'].agg(['count', 'mean']).round(1)
        movies_rating_df.sort_values('count', ascending=False, inplace=True)
        movies_rating_df.rename(columns={'count' : 'Num_ratings', 'mean': 'Average_rating'}, inplace=True)

        C = round(ratings_df['rating'].mean(), 2)
        m = 500
        movies_rating_df['Bayesian_rating'] = (movies_rating_df['Num_ratings'] / (movies_rating_df['Num_ratings'] + m)) * movies_rating_df['Average_rating'] + (m / (movies_rating_df['Num_ratings'] + m)) * C
        movies_rating_df.drop(columns='Average_rating', inplace=True)
        movies_rating_df.rename(columns={'Num_ratings' : 'count', 'Bayesian_rating' : 'weighted_rating'}, inplace=True)
        movies_rating_df.reset_index(inplace=True)
        

        movies_rating_tags_df = pd.merge(movies_rating_df, tags_df, how='left', on='movieId')
        movies_rating_tags_df['tag'] = movies_rating_tags_df['tag'].fillna(value='')
        movies_rating_tags_df = movies_rating_tags_df.groupby(['movieId', 'title', 'genres', 'year', 'url', 'count', 'weighted_rating'])['tag'].apply(list).reset_index()
        movies_rating_tags_df['genres'] = movies_rating_tags_df['genres'].str.split('|')
        movies_rating_tags_df['tag'] = movies_rating_tags_df['tag'].apply(lambda x: [] if x == [float('nan')] else x)
        movies_rating_tags_df.sort_values(by='weighted_rating', ascending=False, inplace=True)
        return movies_rating_tags_df


    def knowledge_based_recommendation(df, user_preferences):
        recommended_movies = df[df['genres'].apply(lambda x: isinstance(x, list) and any(genre in user_preferences['preferred_genres'] for genre in x))]
        print(len(recommended_movies))
        if user_preferences['disliked_genres']:
            recommended_movies = recommended_movies[~recommended_movies['genres'].apply(lambda x: isinstance(x, list) and any(genre in user_preferences['disliked_genres'] for genre in x))]

        print(len(recommended_movies))
        return recommended_movies.head(10)['movieId'].tolist()
    
    def content_based_recommendation(df, last_seen_movies, user_preferences):
        
        df['features'] = df['genres'] + df['tag'] + df['title'].apply(lambda x: [x])  # Add movie titles to features
        df['features'] = df['features'].apply(lambda x: ' '.join(x))  # Ensure 'features' is a string
        tfidf_vectorizer = TfidfVectorizer(stop_words='english')
        tfidf_matrix = tfidf_vectorizer.fit_transform(df['features'])
        cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
        similar_movies_indices = []
        for movie_title in last_seen_movies['liked_movies']:
            movie_indices = df.index[df['title'] == movie_title]
            if len(movie_indices) > 0:
                idx = movie_indices[0]
                similar_movies_indices.extend(cosine_sim[idx].argsort()[-21:-1])  # Get top 20 similar movies
        similar_movies_indices = list(set(similar_movies_indices) - set(df.index[df['title'].isin(last_seen_movies)]))    
        print(similar_movies_indices)    
        if user_preferences['disliked_genres']:
            disliked_genres = user_preferences['disliked_genres']
            similar_movies_indices = [idx for idx in similar_movies_indices if not any(genre in disliked_genres for genre in df.loc[idx, 'genres'])]
        return df.loc[similar_movies_indices[:10], 'movieId'].tolist()

    # def create_utility_matrix(df):
    #     utility_matrix = df.pivot(index='userId', columns='movieId', values='rating').fillna(0)
    #     return utility_matrix


    # def collaborative_filtering_recommendation(df, user_id, k, num_recommendations):
    #     utility_matrix = create_utility_matrix(df)
    #     user_indices = {user_id: idx for idx, user_id in enumerate(utility_matrix.index)}
    #     if user_id not in user_indices:
    #         print("User ID does not exist.")
    #         return []
    #     user_similarity = cosine_similarity(utility_matrix)
    #     knn = NearestNeighbors(n_neighbors=k, metric='cosine')
    #     knn.fit(user_similarity)
    #     _, indices = knn.kneighbors([user_similarity[user_indices[user_id]]])
    #     neighbor_ratings = utility_matrix.iloc[indices[0]]
    #     item_ratings = neighbor_ratings.mean(axis=0)
    #     user_ratings = utility_matrix.loc[user_id]
    #     recommended_items = item_ratings[user_ratings == 0].sort_values(ascending=False).index.tolist()[:num_recommendations]
        
        # # Filter out recommended items based on user preferences
        # if user_preferences['disliked_genres']:
        #     df_filtered = movies_rating_tags_df[~movies_rating_tags_df['genres'].apply(lambda x: any(genre in user_preferences['disliked_genres'] for genre in x))]
        #     recommended_items = [item for item in recommended_items if item in df_filtered['movieId']]
        
        #return movies_rating_tags_df.loc[recommended_items, 'movieId'].tolist()


    def create_X(df):
       
        M = df['userId'].nunique()
        N = df['movieId'].nunique()

        user_mapper = dict(zip(np.unique(df["userId"]), list(range(M))))
        movie_mapper = dict(zip(np.unique(df["movieId"]), list(range(N))))
        
        user_inv_mapper = dict(zip(list(range(M)), np.unique(df["userId"])))
        movie_inv_mapper = dict(zip(list(range(N)), np.unique(df["movieId"])))
        
        user_index = [user_mapper[i] for i in df['userId']]
        item_index = [movie_mapper[i] for i in df['movieId']]

        X = csr_matrix((df["rating"], (user_index,item_index)), shape=(M,N))
        
        return X, user_mapper, movie_mapper, user_inv_mapper, movie_inv_mapper

    


    def collaborative_filtering_recommendation(movie_id, X, movie_mapper, movie_inv_mapper, k, metric='cosine'):
        X = X.T
        neighbour_ids = []
        
        movie_ind = movie_mapper[movie_id]
        movie_vec = X[movie_ind]
        if isinstance(movie_vec, (np.ndarray)):
            movie_vec = movie_vec.reshape(1,-1)
        # use k+1 since kNN output includes the movieId of interest
        kNN = NearestNeighbors(n_neighbors=k+1, algorithm="brute", metric=metric)
        kNN.fit(X)
        neighbour = kNN.kneighbors(movie_vec, return_distance=False)
        for i in range(0,k):
            n = neighbour.item(i)
            neighbour_ids.append(movie_inv_mapper[n])
        neighbour_ids.pop(0)
        return neighbour_ids
    

    # def hybrid_based_recommendation(knowledge_recommendations_ids, content_recommendations_ids, collaborative_recommendations_ids):

    #     recommendations = knowledge_recommendations_ids+content_recommendations_ids+collaborative_recommendations_ids
    
    #     return recommendations
    
    def hybrid_based_recommendation(knowledge_recommendations_ids, content_recommendations_ids, collaborative_recommendations_ids):

        knowledge_weight = 0.6
        content_weight =    0.8
        collaborative_weight = 0.8

        
        num_movies_per_technique_k = int(round(len(knowledge_recommendations_ids) * knowledge_weight))
        num_movies_per_technique_c = int(round(len(content_recommendations_ids) * content_weight))
        num_movies_per_technique_col = int(round(len(collaborative_recommendations_ids) * collaborative_weight))

        
        # Apply weights to each technique's recommendations
        weighted_knowledge_recommendations = knowledge_recommendations_ids[:num_movies_per_technique_k] 
        weighted_content_recommendations = content_recommendations_ids[:num_movies_per_technique_c] 
        weighted_collaborative_recommendations = collaborative_recommendations_ids[:num_movies_per_technique_col] 
        
        # Combine recommendations from all techniques
        combined_recommendations = weighted_knowledge_recommendations + weighted_content_recommendations + weighted_collaborative_recommendations

        
        combined_recommendations = list(set(combined_recommendations))

        
        # # Ensure the total number of recommendations is not more than 10
        combined_recommendations = combined_recommendations
        
        return combined_recommendations
    

    rated_movie_ids = ratings[ratings['userId'] == user_id]['movieId'].unique()
    print(rated_movie_ids)
    movies_rating_tags_df = create_weighted_rating_tags_df(movies, ratings, tags)
    print(len(movies_rating_tags_df))
    movies_rating_tags_df_without_history = movies_rating_tags_df[~movies_rating_tags_df['movieId'].isin(rated_movie_ids)]
    print(len(movies_rating_tags_df))



    user = await session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    preferred_genres = user.genresLike
    disliked_genres = user.genresDislike
    user_preferences = {'preferred_genres': preferred_genres, 'disliked_genres': disliked_genres}

    k_recommendations_ids = knowledge_based_recommendation(movies_rating_tags_df_without_history, user_preferences)
    print(k_recommendations_ids)

    ratings_user = ratings[ratings['userId'] == user_id]

    titles_ids = ratings_user['movieId'].tail(3).tolist()

    title_list = movies_rating_tags_df[movies_rating_tags_df['movieId'].isin(titles_ids)]['title'].tolist()

    user_preferences_movies = {'liked_movies': title_list}

    content_based_recommendations_ids = content_based_recommendation(movies_rating_tags_df, user_preferences_movies, user_preferences)
    print(content_based_recommendations_ids)

    X, user_mapper, movie_mapper, user_inv_mapper, movie_inv_mapper = create_X(ratings)

    collaborative_filtering_recommendations_ids = collaborative_filtering_recommendation(1, X, movie_mapper, movie_inv_mapper, k=10)

    
    print(collaborative_filtering_recommendations_ids)


    recommendations_hybrid = hybrid_based_recommendation(k_recommendations_ids,content_based_recommendations_ids, collaborative_filtering_recommendations_ids)
    
    movies_recommend = movies_rating_tags_df_without_history[movies_rating_tags_df_without_history['movieId'].isin(recommendations_hybrid)]

    print(user_preferences)
    movies_to_recommend = movies_recommend[~movies_recommend['genres'].apply(lambda genres: any(disliked_genre in genres for disliked_genre in user_preferences['disliked_genres']))]

    print(movies_to_recommend[['title', 'genres']])
    return movies_to_recommend.to_dict(orient='records')

def nonPersonalizedToFile():
    script_dir = os.path.dirname(__file__)
    path = os.path.join(script_dir, '../utils/NonPersonalized.json')
    try:
        f = open(path, "x")
        with open(path, "w") as file:
            df = pd.read_sql_query("""SELECT 
            m.movieid,
            m.title,
            m.genres,
            m.imdbid,
            m.year,
            m.url,
            m.titlelower,
            COUNT(r.stars) AS count,
            AVG(r.stars) AS mean
            FROM 
                movie m
            JOIN 
                rating r ON m.movieid = r.movie_id
            GROUP BY 
                m.movieid, m.title, m.genres, m.imdbid, m.year, m.url, m.titlelower""", con=engine)
            m = 1000
            df['weighted_rating'] = ((df['count'] / (df['count'] + m)) * df['mean'] +(m / (df['count'] + m)) * df['mean'].mean())


            sorted_df = df.sort_values(by='weighted_rating', ascending=False)
            json_result = sorted_df.head(5).reset_index().to_dict(orient='records')
            json.dump(json_result, file)
    except:
        print("File already exists")
