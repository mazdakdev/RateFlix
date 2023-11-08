from django.core.management.base import BaseCommand 
from movie.models import Movie, Genre
from multiprocessing.dummy import Pool
import numpy as np
import pandas as pd

class Command(BaseCommand): 
    help = 'Add movies from csv to model'

    def add_arguments(self, parser): 
        parser.add_argument('-S', '--source', type=str, help='Source of Dataset') 
    
    def load_data(self, source, num_processes):

        df = pd.read_csv(source, sep='\t')
    
        all_genres = set(df['genres'].str.split(',').explode().unique())
        self.genre_objects = {}

        for genre_name in all_genres:
            print(f"Genre: Adding: {genre_name}")
            genre, created = Genre.objects.get_or_create(name=genre_name)
            self.genre_objects[genre_name] = genre
            
        df_chunks = np.array_split(df, num_processes)

        pool = Pool(num_processes)
        pool.map(self.process_chunk, df_chunks)
        pool.close()
        pool.join()

    def process_chunk(self, chunk):

        movies = []

        for _, row in chunk.iterrows():
            print(f"Adding {_}-{row['originalTitle']}")

            movie = Movie()

            # set movie fields
            movie.title = row['originalTitle']
            movie.tconst = row['tconst']
            movie.is_adult = row['isAdult']

            if row['startYear'] != "\\N":
                movie.start_year = row['startYear']

            movie_genres = row['genres'].split(',')
            movie.save()

            genres = [self.genre_objects[g] for g in row['genres'].split(',')]  
            movie.genres.add(*genres)
            movie.save()

            movies.append(movie)
            

    def handle(self, *args, **kwargs):
        self.load_data(kwargs["source"], 4)

#TODO: handle sereies episdoes
#TODO: use Threads