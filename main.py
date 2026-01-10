import json
from typing import Optional
from fastapi import FastAPI
# git add .
# git commit -m "message"
# git push origin main
# https://dailyreminderapi.onrender.com
# https://dailyreminderapi.onrender.com/items/12
# https://dashboard.render.com/web/srv-d5hc3jadbo4c73dtsh3g/deploys/dep-d5hcstq4d50c7390mlk0


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "Lightsaber": q}

@app.get("/settings/")
def get_settings():
    read_file("settings.txt")
    return read_file("settings.txt")

@app.put("/settings/")
def update_item(data: dict):
    #if data["kyber"]=="crystal":
        #del data["kyber"]
    json_string = json.dumps(data)
    save_file("settings.txt",json_string)
    return {
        "message": "Received dictionary",
        "received":json_string
        }

def save_file(file_path:str,file_content:str):
    try:
        with open(file_path, "w") as file:
            file.write(file_content)
    except Exception as e:
        return f"An error occurred while saving the file: {e}"

def read_file(file_path:str)->str:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            return content
    except FileNotFoundError:
        return f"Error: The file '{file_path}' was not found."
    except Exception as e:
        return f"An error occurred while reading the file: {e}"