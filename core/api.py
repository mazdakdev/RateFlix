from fastapi import FastAPI
import csv

app = FastAPI()

@app.get("/api/v1/movies")
async def search(title: str):
    results = []
    with open('../models/movies.csv', 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        for row in csv_reader:
            for cell in row:
                if title.lower() in cell.lower():
                    results.append(dict(zip(header, row)))
                    break

    return {"code":0, "results": results}
