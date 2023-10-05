import pandas as pd
from math import sqrt

class MovieRecommender:
    def __init__(self, movies_path, ratings_path):
        self.movies_df = pd.read_csv(movies.csv)
        self.ratings_df = pd.read_csv(ratings.csv)

    def _preprocess_movies(self):
        self.movies_df['year'] = self.movies_df.title.str.extract('(\(\d\d\d\d\))',expand=False)
        self.movies_df['year'] = self.movies_df.year.str.extract('(\d\d\d\d)',expand=False)
        self.movies_df['title'] = self.movies_df.title.str.replace('(\(\d\d\d\d\))', '')
        self.movies_df['title'] = self.movies_df['title'].apply(lambda x: x.strip())
        self.movies_df = self.movies_df.drop('genres', 1)

    def _preprocess_ratings(self):
        self.ratings_df = self.ratings_df.drop('timestamp', 1)

    def _get_user_input(self, userInput):
        inputMovies = pd.DataFrame(userInput)
        inputId = self.movies_df[self.movies_df['title'].isin(inputMovies['title'].tolist())]
        inputMovies = pd.merge(inputId, inputMovies)
        return inputMovies.drop('year', 1)

    def _filter_user_subset(self, inputMovies):
        userSubset = self.ratings_df[self.ratings_df['movieId'].isin(inputMovies['movieId'].tolist())]
        return userSubset

    def _calculate_pearson_correlation(self, userSubsetGroup, inputMovies):
        pearsonCorrelationDict = {}
        
        for name, group in userSubsetGroup:
            group = group.sort_values(by='movieId')
            inputMovies = inputMovies.sort_values(by='movieId')

            nRatings = len(group)
            temp_df = inputMovies[inputMovies['movieId'].isin(group['movieId'].tolist())]
            tempRatingList = temp_df['rating'].tolist()
            tempGroupList = group['rating'].tolist()

            Sxx = sum([i**2 for i in tempRatingList]) - pow(sum(tempRatingList),2)/float(nRatings)
            Syy = sum([i**2 for i in tempGroupList]) - pow(sum(tempGroupList),2)/float(nRatings)
            Sxy = sum(i*j for i, j in zip(tempRatingList, tempGroupList)) - sum(tempRatingList)*sum(tempGroupList)/float(nRatings)

            if Sxx != 0 and Syy != 0:
                pearsonCorrelationDict[name] = Sxy/sqrt(Sxx*Syy)
            else:
                pearsonCorrelationDict[name] = 0
        
        return pearsonCorrelationDict

    def predict(self, userInput):
        self._preprocess_movies()
        self._preprocess_ratings()

        inputMovies = self._get_user_input(userInput)
        userSubset = self._filter_user_subset(inputMovies)
        userSubsetGroup = userSubset.groupby(['userId'])

        pearsonCorrelationDict = self._calculate_pearson_correlation(userSubsetGroup, inputMovies)

        pearsonDF = pd.DataFrame.from_dict(pearsonCorrelationDict, orient='index')
        pearsonDF.columns = ['similarityIndex']
        pearsonDF['userId'] = pearsonDF.index
        pearsonDF.index = range(len(pearsonDF))

        topUsers = pearsonDF.sort_values(by='similarityIndex', ascending=False)[0:50]
        topUsersRating = topUsers.merge(self.ratings_df, left_on='userId', right_on='userId', how='inner')

        topUsersRating['weightedRating'] = topUsersRating['similarityIndex'] * topUsersRating['rating']

        tempTopUsersRating = topUsersRating.groupby('movieId').sum()[['similarityIndex', 'weightedRating']]
        tempTopUsersRating.columns = ['sum_similarityIndex', 'sum_weightedRating']

        recommendation_df = pd.DataFrame()
        recommendation_df['weighted average recommendation score'] = tempTopUsersRating['sum_weightedRating'] / tempTopUsersRating['sum_similarityIndex']
        recommendation_df['movieId'] = tempTopUsersRating.index

        recommendation_df = recommendation_df.sort_values(by='weighted average recommendation score', ascending=False)

        return recommendation_df.merge(self.movies_df, left_on='movieId', right_on='movieId').head(10)

# Example usage
recommender = MovieRecommender('movies.csv', 'ratings.csv')
user_input = [
    {'title': 'Breakfast Club, The', 'rating': 5},
    {'title': 'Toy Story', 'rating': 3.5},
    {'title': 'Jumanji', 'rating': 2},
    {'title': "Pulp Fiction", 'rating': 5},
    {'title': 'Akira', 'rating': 4.5}
]
result = recommender.predict(user_input)
print(result)
