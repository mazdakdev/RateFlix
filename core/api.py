from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi import status, HTTPException
from models.recommender.helper import MovieRecommender
from models.sentimentLSTM.helper import CommentAnalyzer
from pydantic import BaseModel
import random
import re
import csv
import json

app = FastAPI()

recommender = MovieRecommender(
        movies_df="models/recommender/movies.csv", 
        ratings_df="models/recommender/ratings.csv"
    )

comment_analyzer = CommentAnalyzer(
    model_path = "models/sentimentLSTM/state_dict.pt",
    vocab_path = "models/sentimentLSTM/vocab.pkl"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Movie(BaseModel):
    movies: list

@app.get("/api/v1/movies")
async def search(title: str, offset: int = 0, limit: int = 5):
    results = []
    with open('models/recommender/movies.csv', 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        count = 0
        for row in csv_reader:
            for cell in row:
                if title.lower() in cell.lower():
                    if count >= offset:
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
async def analyse(comment: str):
    score = comment_analyzer.predict(comment)
    score = round(score, 2)

    return {"score": score}
    

@app.post("/api/v1/recommend")
async def recommend(movies: Movie):
        user_input = movies.movies
        recommended_list = recommender.recommend(user_input).to_json(orient="records") 

        return recommended_list 