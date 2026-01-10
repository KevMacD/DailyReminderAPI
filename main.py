from typing import Optional

from fastapi import FastAPI
# git add .
# git commit -m "message"
# git push origin main
# https://dailyreminderapi.onrender.com
# https://dailyreminderapi.onrender.com/items/123


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "Lightsaber": q}

@app.get("/settings/")
def get_settings():
    return {"is_logging": False}

@app.put("/settings/")
def update_item(data: dict):
    return {
        "message": "Received dictionary",
        "received": data
    }