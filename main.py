from typing import Optional

from fastapi import FastAPI
# git add .
# git commit -m "message"
# git push origin main



app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "Kyber Crystals": q}