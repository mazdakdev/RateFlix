from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import status, HTTPException
import re
import csv

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:8081']
)

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
                        row[1] = re.sub(r'\(\d+\)', '', row[1]).strip()
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
