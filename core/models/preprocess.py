import pandas

movies_df = pandas.read_csv("movies.csv")
ratings_df = pandas.read_csv("ratings.csv")

movies_df['year'] = movies_df.title.str.extract('(\(\d\d\d\d\))', expand=False)
movies_df['year'] = movies_df.year.str.extract('(\d\d\d\d)', expand=False)
movies_df['title'] = movies_df.title.str.replace('(\(\d\d\d\d\))', '', regex=True)
movies_df['title'] = movies_df['title'].apply(lambda x: x.strip())
movies_df = movies_df.drop('genres', axis=1)


ratings_df = ratings_df.drop('timestamp', axis=1)

movies_df.to_csv("movies.csv", index=False)
ratings_df.to_csv("ratings.csv", index=False)

#TODO: Foo, the must be The Foo