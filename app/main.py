from fastapi import FastAPI

app = FastAPI()


@app.get("/hotels/{hotels_id}")
async def hotel(hotels_id: int, date_from, date_to):
    return hotels_id, date_from, date_to
