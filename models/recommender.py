import pandas as pd
from math import sqrt

class MovieRecommender:
    def __init__(self, movies_df, ratings_df):
        self.movies_df = pd.read_csv(movies_df)
        self.ratings_df = pd.read_csv(ratings_df)
        self.preprocess_movies()
        self.preprocess_ratings()

    def preprocess_movies(self):
        self.movies_df['year'] = self.movies_df.title.str.extract('(\(\d\d\d\d\))', expand=False)
        self.movies_df['year'] = self.movies_df.year.str.extract('(\d\d\d\d)', expand=False)
        self.movies_df['title'] = self.movies_df.title.str.replace('(\(\d\d\d\d\))', '', regex=True)
        self.movies_df['title'] = self.movies_df['title'].apply(lambda x: x.strip())
        self.movies_df = self.movies_df.drop('genres', axis=1)

    def preprocess_ratings(self):
        self.ratings_df = self.ratings_df.drop('timestamp', axis=1)

    def get_user_input_dataframe(self, user_input):
        input_movies = pd.DataFrame(user_input)
        input_id = self.movies_df[self.movies_df['title'].isin(input_movies['title'].tolist())]
        input_movies = pd.merge(input_id, input_movies)
        input_movies = input_movies.drop('year', axis=1)
        return input_movies

    def filter_user_subset(self, input_movies):
        user_subset = self.ratings_df[self.ratings_df['movieId'].isin(input_movies['movieId'].tolist())]
        return user_subset

    def calculate_pearson_correlation(self, user_subset_group, input_movies):
        pearson_correlation_dict = {}

        for name, group in user_subset_group:
            group = group.sort_values(by='movieId')
            input_movies_subset = input_movies[input_movies['movieId'].isin(group['movieId'].tolist())]

            n_ratings = len(group)
            temp_rating_list = input_movies_subset['rating'].tolist()
            temp_group_list = group['rating'].tolist()

            sxy = sum([i * j for i, j in zip(temp_rating_list, temp_group_list)]) - (sum(temp_rating_list) * sum(temp_group_list)) / float(n_ratings)
            sxx = sum([i**2 for i in temp_rating_list]) - pow(sum(temp_rating_list), 2) / float(n_ratings)
            syy = sum([i**2 for i in temp_group_list]) - pow(sum(temp_group_list), 2) / float(n_ratings)

            if sxx != 0 and syy != 0:
                pearson_correlation_dict[name] = sxy / sqrt(sxx * syy)
            else:
                pearson_correlation_dict[name] = 0

        return pd.DataFrame.from_dict(pearson_correlation_dict, orient='index', columns=['similarityIndex'])


    def recommend_movies(self, top_users, user_subset):
        top_users_rating = pd.concat([top_users, self.ratings_df], join='inner', axis=1)
        top_users_rating['weightedRating'] = top_users_rating['similarityIndex'] * top_users_rating['rating']
        temp_top_users_rating = top_users_rating.groupby('movieId').sum()[['similarityIndex', 'weightedRating']]
        temp_top_users_rating.columns = ['sum_similarityIndex', 'sum_weightedRating']

        recommendation_df = pd.DataFrame()
        recommendation_df['weighted average recommendation score'] = temp_top_users_rating['sum_weightedRating'] / temp_top_users_rating['sum_similarityIndex']
        recommendation_df['movieId'] = temp_top_users_rating.index

        return recommendation_df.sort_values(by='weighted average recommendation score', ascending=False)

    def recommend(self, user_input):
        input_movies = self.get_user_input_dataframe(user_input)
        user_subset = self.filter_user_subset(input_movies)
        user_subset_group = user_subset.groupby(['userId'])
        
        pearson_df = self.calculate_pearson_correlation(user_subset_group, input_movies)
        pearson_df['userId'] = pearson_df.index
        pearson_df.index = range(len(pearson_df))

        top_users = pearson_df.sort_values(by='similarityIndex', ascending=False).head(50)
        recommendation_df = self.recommend_movies(top_users, user_subset)

        return self.movies_df.loc[self.movies_df['movieId'].isin(recommendation_df.head(10)['movieId'].tolist())]



# Example Usage:
movies_file = 'movies.csv'
ratings_file = 'ratings.csv'
recommender = MovieRecommender(movies_file, ratings_file)

user_input = [
    {'title': 'Breakfast Club, The', 'rating': 5},
    {'title': 'Toy Story', 'rating': 3.5},
    {'title': 'Jumanji', 'rating': 2},
    {'title': "Pulp Fiction", 'rating': 5},
    {'title': 'Akira', 'rating': 4.5}]

recommendations = recommender.recommend(user_input)
print(recommendations)
