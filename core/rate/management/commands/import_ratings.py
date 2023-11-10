from django.core.management.base import BaseCommand 
from movie.models import Movie
from multiprocessing.dummy import Pool
from rate.models import Rate
import numpy as np
import pandas as pd

class Command(BaseCommand): 
    help = 'Add ratings and users from csv to model'

    def add_arguments(self, parser): 
        parser.add_argument('-S', '--source', type=str, help='Source of Dataset') 
    
    def load_data(self, source, num_processes):

        df = pd.read_csv(source)
            
        df_chunks = np.array_split(df, num_processes)

        pool = Pool(num_processes)
        pool.map(self.process_chunk, df_chunks)
        pool.close()
        pool.join()

    def process_chunk(self, chunk):
        for _, row in chunk.iterrows():
            if row['movieId']:
                print(f"Adding {_}-for user {row['userId']}")

                rating = Rate()
                rating.imdb_user = row['userId']
                rating.rating = row['rating']
                rating.timestamp = row['timestamp']
                rating.save()

                movie_id = row['movieId']
                try:
                    rating.movie = Movie.objects.get(id=movie_id)
                except Movie.DoesNotExist:
                    print(f"Movie with id {movie_id} does not exist")
                    continue

                rating.save()

            

    def handle(self, *args, **kwargs):
        self.load_data(kwargs["source"], 20)

#TODO: use Threads instead of Multiprocessing.dummy