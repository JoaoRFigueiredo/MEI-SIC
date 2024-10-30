import pandas as pd
import os

script_dir = os.path.dirname(__file__)
movies_df = pd.read_csv(os.path.join(script_dir, "./small_dataset/movies_full_2.csv"))
ratings_df = pd.read_csv(os.path.join(script_dir, "./small_dataset/ratings.csv"))
ratings_df.drop('timestamp', axis=1, inplace=True)
movies_df['decade'] = (movies_df['year'] // 10) * 10
movies_rating_user_df = pd.merge(movies_df, ratings_df, on="movieId", how="inner")

# Mantém o movieId como coluna, não como parte do índice
movies_rating_df = movies_rating_user_df[['movieId', 'title', 'rating', 'genres', 'year', 'decade', 'url']].groupby(
    ['movieId', 'title', 'genres', 'year', 'decade', 'url']
)['rating'].agg(['count', 'mean']).round(1).reset_index()

movies_rating_df.sort_values('count', ascending=False, inplace=True)
movies_rating_df.rename(columns={'count': 'Num_ratings', 'mean': 'Average_rating'}, inplace=True)

def calculate_weighted_rating(df, C, m):
    """
    Calculate Bayesian weighted rating for each movie in the DataFrame.

    Parameters:
    df (DataFrame): DataFrame containing movie ratings.
    C (float): Average rating across all movies (prior assumption).
    m (int): Minimum number of ratings required to be considered.

    Returns:
    DataFrame: DataFrame with Bayesian weighted rating column added.
    """
    
    # Add the Bayesian weighted rating as a new column in the DataFrame
    df['Bayesian_rating'] = (df['Num_ratings'] / (df['Num_ratings'] + m)) * df['Average_rating'] + (m / (df['Num_ratings'] + m)) * C

    return df

C = round(ratings_df['rating'].mean(), 2)
movies_rating_df = calculate_weighted_rating(movies_rating_df, C, 500)
movies_rating_df.drop(columns='Average_rating', inplace=True)
movies_rating_df.sort_values(by='Bayesian_rating', ascending=False, inplace=True)

movies_rating_df.rename(columns={'Num_ratings': 'count', 'Bayesian_rating' : 'weighted_rating'}, inplace=True)

# Salva o DataFrame no CSV, incluindo movieId
movies_rating_df.to_csv(os.path.join(script_dir, "./small_dataset/movies_rating.csv"), index=False)
