from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi import status, HTTPException
from typing import Dict, Any
from models.recommender import MovieRecommender
from pydantic import BaseModel
import random
import re
import csv
import json

app = FastAPI()
recommender = MovieRecommender("models/movies.csv", "models/ratings.csv")

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:8081']
)

class Movie(BaseModel):
    movies: list

@app.get("/api/v1/movies")
async def search(title: str, offset: int = 0, limit: int = 5):
    results = []
    with open('../models/movies.csv', 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        count = 0
        for row in csv_reader:
            for cell in row:
                if title.lower() in cell.lower():
                    if count >= offset:
                        row[1] = re.sub(r'\(\d+\)', '', row[1]).strip() #remove (year) from title
                        parts = row[1].split(",")
                        if len(parts) == 2:
                            row[1] = parts[1] + " " + parts[0]  # change foo, The to The foo
                        results.append(dict(zip(header, row)))
                    count += 1
                    break
            if len(results) >= limit:
                break
    if results:
        return {"code":0, "results": results}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'The Query Had No Result !',
    )


@app.get("/api/v1/score")
async def search(comment: str):
    return {"score": random.randrange(0,5)}
    
    #TODO: Must get the score from the sentiment model saved in pickle file

@app.post("/api/v1/recommend")
async def search(movies: Movie):
    user_input = movies.movies
    recommended_list = recommender.recommend(user_input).to_json(orient="records") 

    return recommended_list

#TODO: the csv must be preprocessed before running 